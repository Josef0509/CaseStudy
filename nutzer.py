import streamlit as st
import datetime
import time
from st_pages import add_page_title
from class_user import User
import queries
import pandas as pd

# Initialize session state
if 'show_session' not in st.session_state:
    st.session_state.show_session = False

if 'delete' not in st.session_state:
	st.session_state.delete = False

#adding the page title
add_page_title()

#creating placeholders for the input fields
name_ph = st.empty()
email_ph = st.empty()
cl1, cl2 = st.columns(2)
button1_ph = cl1.empty()
button2_ph = cl2.empty()

if not st.session_state.show_session:
	#creating a dropdown menu with all devices
	user_name = name_ph.text_input("Name des Nutzers:", placeholder="Max Mustermann")
	user_email = email_ph.text_input("E-Mail-Adresse des Nutzers:", placeholder="E-Mail-Adresse")


	# Nutzer speichern
	if button1_ph.button("Nutzer anlegen"):
		if user_name == "" or user_email == "":
			st.warning("Bitte alle Felder ausfüllen!")
			time.sleep(2)
			st.rerun()
		else:
			#Store the user data in a dictionary
			data_user = User(user_name, user_email)
			data_user.store_data()

			with st.spinner("Loading..."):
				time.sleep(1)
				#Save the user
			st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")
			time.sleep(2)
			st.rerun()

	if button2_ph.button("Nutzer anzeigen"):
		st.session_state.show_session = True


# Nutzerdaten anzeigen
if st.session_state.show_session:

	#Empty the input fields
	name_ph.empty()
	email_ph.empty()
	button1_ph.empty()
	button2_ph.empty()
	del_index = 0

	users = queries.find_database('users', 'name')
	print(users)
	if users:
		data_list = []
		for user in users[0]:
			user_data = User.load_data_by_user_name(user)
			#print(user_data)
			if user_data:
				data_list.append({"ID": user_data[1], "Nutzer": user_data[0].name, "Email": user_data[0].email, "Löschen": user_data[0].is_active})
		# Show data
		df = pd.DataFrame(data_list)
		edited_df = name_ph.data_editor(df, disabled= ("ID", "Nutzer", "Email"), hide_index=True, on_change= None)

		del_index = edited_df.loc[edited_df["Löschen"].idxmax()]["ID"]
		#print(del_index)
	else:
		name_ph.error("Keine gültigen Nutzer gefunden!")

	if button1_ph.button("Nutzer löschen"):
		try:
			with st.spinner("Loading..."):
				if queries.find_database('devices', 'managed_by_user_id'):
					raise Exception("Nutzer kann nicht gelöscht werden, da er noch Geräte zugewiesen hat!")
				if queries.find_database('reservations', 'reserver'):
					raise Exception("Nutzer kann nicht gelöscht werden, da er noch Reservierungen zugewiesen hat!")
				User.delete_data_by_doc_id(del_index)
				st.session_state.show_session = False
				time.sleep(1)
		except Exception as e:
			st.error(e)
			time.sleep(1)
			st.rerun()
		st.success(f"Nutzer wurde gelöscht!")
		time.sleep(2)
		st.rerun()

	if button2_ph.button("Zurück"):
		name_ph.empty()
		button1_ph.empty()
		button2_ph.empty()
		st.session_state.show_session = False
		st.rerun()