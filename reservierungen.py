import streamlit as st
import time
from st_pages import add_page_title
import pandas as pd


# Initialize session state
if 'show_session' not in st.session_state:
    st.session_state.show_session = False

#adding the page title
add_page_title()

#creating placeholders for the input fields
name_ph = st.empty()
reserver_ph = st.empty()
cl1, cl2 = st.columns(2)
date_start_ph = cl1.empty()
date_end_ph = cl2.empty()
time_start_ph = st.empty()
time_end_ph = st.empty()
cl3, cl4 = st.columns(2)
button1_ph = cl3.empty()
button2_ph = cl4.empty()


#creating a dropdown menu with all devices
if not st.session_state.show_session:

	device_name = name_ph.selectbox("Gerät:", ["Ger\u00E4t 1", "Ger\u00E4t 2", "Ger\u00E4t 3"], placeholder="Ger\u00E4t ausw\u00E4hlen ...")
	reserver = reserver_ph.selectbox("Reservierende Person:", ["Person 1", "Person 2", "Person 3"])
	reservation_date_start = date_start_ph.date_input("Reservierungsanfangsdatum:")
	reservatio_date_end = date_end_ph.date_input("Reservierungsenddatum:")
	start_time = time_start_ph.time_input("Anfangszeit:")
	end_time = time_end_ph.time_input("Endzeit:")

	# Weitere Reservierungsattribute hier hinzufügen
	if button1_ph.button("Speichern"):
		#Store the reservation data in a dictionary
		reservation_data = {
			"device_id": device_name,
			"reservation_date_start": reservation_date_start,
			"reservation_date_end": reservatio_date_end,
			"reserver": reserver,
			"start_time": start_time,
			"end_time": end_time
			# Weitere Reservierungsattribute hier hinzufügen
		}
		# Loading message
		with st.spinner("Loading..."):
				time.sleep(1)

		# Message that the reservation was created
		st.success(f"Reservierung von {device_name} wurde für {reserver} zwischen {reservation_date_start} - {reservatio_date_end} von {start_time} bis {end_time} angelegt!")

	if button2_ph.button("Löschen"):
		st.session_state.show_session = True
		button1_ph.empty()
		button2_ph.empty()


if st.session_state.show_session:
	reservation_data = pd.DataFrame(
		{
			"device_id": ["Gerät 1", "Gerät 2", "Gerät 3", "Gerät 4"],
			"reservation_date_start": ["2021-06-01", "2021-06-01", "2021-06-01", "2021-06-01"],
			"reservation_date_end": ["2021-06-01", "2021-06-01", "2021-06-01", "2021-06-01"],
			"reserver": ["Stefan Posch", "Josef Obwaller", "Sandro Streicher", "Elias Zischg"],
			"start_time": ["08:00", "09:00", "10:00", "11:00"],
			"end_time": ["09:00", "10:00", "11:00", "12:00"],
		}
	)

	name_ph.data_editor(
		reservation_data,
		column_config={
			"device_id": st.column_config.ListColumn("Liste der Nutzer", width="medium"),
			"reservation_date_start": st.column_config.TextColumn("Reservierungsanfangsdatum", width="medium"),
			"reservation_date_end": st.column_config.TextColumn("Reservierungsenddatum", width="medium"),
			"reserver": st.column_config.TextColumn("Reservierende Person", width="medium"),
			"start_time": st.column_config.TextColumn("Anfangszeit", width="medium"),
			"end_time": st.column_config.TextColumn("Endzeit", width="medium"),
		},
		hide_index=True,
	)

	reserver_ph.empty()
	date_start_ph.empty()
	date_end_ph.empty()
	time_start_ph.empty()
	time_end_ph.empty()

	if button1_ph.button("Reservierung löschen"):
		# Loading message
		with st.spinner("Loading..."):
			time.sleep(1)
		# Message that the reservation was deleted
		st.success("Reservierung wurde gelöscht!")
		time.sleep(2)
		st.session_state.show_session = False
		st.rerun()

	if button2_ph.button("Zurück"):
		st.session_state.show_session = False
		st.rerun()
