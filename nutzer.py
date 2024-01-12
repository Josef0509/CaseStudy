import streamlit as st
import datetime
import time
from st_pages import add_page_title
from class_user import User

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
user_name = name_ph.text_input("Name des Nutzers:")
user_email = email_ph.text_input("E-Mail-Adresse des Nutzers:")


# Nutzer speichern
if button1_ph.button("Nutzer anlegen"):
	#Store the user data in a dictionary
	User(user_name, user_email)
	User.store_data()

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
	# Load data
	User.load_data_by_user_name(user_name)
	# Show data
	table_ph.data_editor( data_df, column_config=
	{
		"Nutzer": st.column_config.ListColumn( "Nutzername", width="medium",),
		"Email": st.column_config.ListColumn( "E-Mail", width="medium",),
	},
	hide_index=True,
	)
	# Hide data
	if button2_ph.button("Nutzer ausblenden"):
		table_ph.empty()