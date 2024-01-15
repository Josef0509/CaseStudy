import streamlit as st
import datetime
import time
from st_pages import add_page_title
from class_user import User
import queries

# Initialize session state
if 'show_session' not in st.session_state:
    st.session_state.show_session = False

#adding the page title
add_page_title()

#creating placeholders for the input fields
name_ph = st.empty()
email_ph = st.empty()
cl1, cl2 = st.columns(2)
button1_ph = cl1.empty()
button2_ph = cl2.empty()
table_ph = st.empty()

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


# Nutzerdaten anzeigen
if button2_ph.button("Nutzer anzeigen"):
	# Empty placeholder
	button2_ph.empty()
	users = queries.find_database('users', 'name')

	if users:
		data_list = []
		for user in users:
			user_data = User.load_data_by_user_name(user)
			if user_data:
				data_list.append({"Nutzer": user_data.name, "Email": user_data.email})
		# Show data
		table_ph.data_editor( data_list, column_config= {"Nutzer": st.column_config.ListColumn( "Nutzername", width="medium",), "Email": st.column_config.ListColumn( "E-Mail", width="medium",),} ,hide_index=True)
		# Hide data
		if button2_ph.button("Nutzer ausblenden"):
			table_ph.empty()
	else:
		st.error("Keine gültigen Nutzer gefunden!")
		time.sleep(2)
		st.rerun()
