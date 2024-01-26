import streamlit as st
import time
from st_pages import add_page_title
import pandas as pd
import queries
from class_reservation import Reservation
from datetime import datetime


# Initialize session state
if 'show_session' not in st.session_state:
    st.session_state.show_session = False

#adding the page title
add_page_title()

#creating placeholders for the input fields
name_ph = st.empty()
table_ph = st.empty()
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
	reservation_data = []
	users = queries.find_database('users', 'name')
	devices = queries.find_database('devices', 'device_name')

	device_name = name_ph.selectbox("Gerät:", ["", *devices[0]], index=0, key = "device_name_reservierung")
	# Load the reservation data from the database
	try:
		data_res = Reservation.load_data_by_device_name(device_name)
		for i in range(len(data_res)):
			#print(f"Device: {data_res[0][i].device_name}, Reserver: {data_res[0][i].reserver}, Start: {data_res[0][i].start_time}, End: {data_res[0][i].end_time}")
			reservation_data.append({"ID" : data_res[1], "Gerät" : data_res[0][i].device_name, "Nutzer" : data_res[0][i].reserver, "Reservierungsanfang" : data_res[0][i].start_time.strftime("%Y-%m-%d %H:%M:%S"), "Reservierungsende" : data_res[0][i].end_time.strftime("%Y-%m-%d %H:%M:%S"), "Löschen" : data_res[0][i].is_active})
	except LookupError as e:
		table_ph.text("Keine Reservierungen vorhanden!")
	#Print the table
	if not reservation_data == []:
		df = pd.DataFrame(reservation_data)
		edited_df = table_ph.data_editor( df, disabled=("ID", "Gerät", "Nutzer", "Reservierungsanfang", "Reservierungsende"), hide_index=True, on_change= None)
		# Delete the reservation
		del_index = edited_df.loc[edited_df["Löschen"].idxmax()]["ID"]

  
	reserver = reserver_ph.selectbox("Reservierende Person:", ["", *users[0]], index=0)
	reservation_date_start = date_start_ph.date_input("Reservierungsanfangsdatum:", value=None)
	reservation_date_end = date_end_ph.date_input("Reservierungsenddatum:", value=None)
	start_time = time_start_ph.time_input("Anfangszeit:", value=None)
	end_time = time_end_ph.time_input("Endzeit:", value=None)


	# Weitere Reservierungsattribute hier hinzufügen
	if button1_ph.button("Speichern"):
		#Combine the date and time
		try:
			temp_start = datetime.combine(reservation_date_start, start_time)
			temp_stop = datetime.combine(reservation_date_end, end_time)
		except Exception as e:
			pass

		try:
			if temp_start > temp_stop:
				raise LookupError("Reservierungsanfangsdatum muss vor dem Reservierungsenddatum liegen!")
		except Exception as e:
			st.error(e)
			time.sleep(2)
			st.rerun()
		# Store the reservation data in the database
		Reser = Reservation(device_name, reserver, temp_start, temp_stop)
		# Loading message
		try:
			with st.spinner("Loading..."):
				Reser.store_data()
		except LookupError as e:
			st.error(e)
			time.sleep(2)
			st.rerun()
			# Message that the reservation was created
		st.success(f"Reservierung von {device_name} wurde für {reserver} zwischen {reservation_date_start} - {reservation_date_end} von {start_time} bis {end_time} angelegt!")
		time.sleep(2)
		st.rerun()

	if button2_ph.button("Reservierung löschen"):
		# Loading message
		with st.spinner("Loading..."):
			Reservation.delete_data_by_doc_id(del_index)
			time.sleep(1)
		# Message that the reservation was deleted
		st.success("Reservierung wurde gelöscht!")
		time.sleep(2)
		st.rerun()

