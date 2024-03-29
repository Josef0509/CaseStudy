import streamlit as st
from datetime import datetime
import time
from st_pages import add_page_title
from class_devices import Device
import queries

# Initialize session state
if 'show_session' not in st.session_state:
    st.session_state.show_session = 0

#adding the page title
add_page_title()

#creating placeholders for the input fields
header_ph = st.empty()
device_ph = st.empty()
article_number_ph = st.empty()
acquisition_date_ph = st.empty()
description_ph = st.empty()
responsible_person_ph = st.empty()
cl1, cl2, cl3 = st.columns(3)
button1_ph = cl1.empty()
button2_ph = cl2.empty()
button3_ph = cl3.empty()

if st.session_state.show_session == 0:
	# Find the users
	person_data = queries.find_database('users', 'name')

	#Create a menu to assign a new machine
	header_ph.header("Neues Gerät anlegen")
	device_name = device_ph.text_input("Name des Geräts*:")
	article_number = article_number_ph.text_input("Artikelnummer*:")
	acquisition_date = datetime.now().strftime("%Y-%m-%d")
	change_date = datetime.now().strftime("%Y-%m-%d")
	device_description = description_ph.text_area("Optionale Beschreibung:")
	device_responsible = responsible_person_ph.selectbox("verantwortliche Person*:",["", *person_data[0]], index=0)

	if button1_ph.button("Gerät anlegen"):
		if device_name == "" or article_number == "":
			st.warning("Bitte alle Pflichtfelder (*) ausfüllen!")
			time.sleep(2)
		else:
			data = Device(device_name, article_number, device_description, device_responsible, acquisition_date, change_date)
			data.store_data()

			with st.spinner("Loading..."):
				time.sleep(1)
				#Save the device

				st.success(f"Gerät {device_name} mit dem Verantwortlichen {device_responsible} wurde angelegt!")
		time.sleep(2)
		st.rerun()

	if button2_ph.button("Gerät ändern"):
		st.session_state.show_session = 1
		header_ph.empty()
		device_ph.empty()
		article_number_ph.empty()
		acquisition_date_ph.empty()
		description_ph.empty()
		responsible_person_ph.empty()
		button1_ph.empty()
		button2_ph.empty()
		button3_ph.empty()
		st.rerun()

	if button3_ph.button("Geräte anzeigen"):
		st.session_state.show_session = 2
		header_ph.empty()
		device_ph.empty()
		article_number_ph.empty()
		acquisition_date_ph.empty()
		description_ph.empty()
		responsible_person_ph.empty()
		button1_ph.empty()
		button2_ph.empty()
		button3_ph.empty()
		st.rerun()

if st.session_state.show_session == 1:
	header_ph.header("Gerät ändern")
	devices = queries.find_database('devices', 'device_name')
	#print(devices)
	users = queries.find_database('users', 'name')
	try:
		device_name = device_ph.selectbox("Gerät:", devices[0], placeholder="Gerät auswählen ...")
		device_data = Device.load_data_by_device_name(device_name)
		#print(device_data[0].device_name)
		# Fill the placeholders with the data of the selected device
		art_number = article_number_ph.text_input("Artikelnummer:", value = device_data[0].article_number)
		acquisition_date_ph.text(device_data[0].acquisition_date)
		cdate = datetime.now().strftime("%Y-%m-%d")
		description = description_ph.text_area("Optionale Beschreibung:", value = device_data[0].device_description)
		manager = responsible_person_ph.selectbox("verantwortliche Person:", users[0], index = users[0].index(device_data[0].managed_by_user_id))

		if button1_ph.button("Gerät ändern"):
		#Store the reservation data the Device class to secure a smooth data transfer
			device_data[0].article_number = art_number
			device_data[0].change_date = cdate
			device_data[0].device_description = description
			device_data[0].managed_by_user_id = manager
			device_data[0].store_data()
			with st.spinner("Loading..."):
				time.sleep(1)
				#Save the device
			st.success(f"Gerät {device_data[0].device_name} mit dem Verantwortlichen {device_data[0].managed_by_user_id} wurde aktualisiert!")
			time.sleep(2)
			st.session_state.show_session = 0
			st.rerun()
	except Exception as e:
		device_ph.text("Keine Geräte vorhanden!")

	if button2_ph.button("Zurück"):
		st.session_state.show_session = 0
		st.rerun()

if st.session_state.show_session == 2:
	header_ph.header("Geräte anzeigen")
	devices = queries.find_database('devices', 'device_name')
	index = 0
	try:
		list_of_tabs = st.tabs(devices[0])



		for i in range(len(list_of_tabs)):
			with list_of_tabs[i]:
				device_data = Device.load_data_by_device_name(devices[0][i])

				index = devices[1][i]
				st.title(device_data[0].device_name)
				st.text("ID: " + device_data[0].article_number)
				st.text("Verantwortliche Person: " + device_data[0].managed_by_user_id)
				st.text("Beschreibung: " + device_data[0].device_description)
				st.text("letzte Änderung: " + device_data[0].change_date)
				st.text("Anschaffungsdatum: " + device_data[0].acquisition_date)

	except Exception as e:
		device_ph.text("Keine Geräte vorhanden!")

	if button1_ph.button("Zurück"):
		st.session_state.show_session = 0
		st.rerun()

	if button3_ph.button("Gerät löschen"):
		try:
			Device.delete_data_by_doc_id(index)
			st.session_state.show_session = 0
		except Exception as e:
			st.error(e)
			time.sleep(2)
			st.rerun()
			
		header_ph.empty()
		device_ph.empty()
		article_number_ph.empty()
		acquisition_date_ph.empty()
		description_ph.empty()
		responsible_person_ph.empty()
		button1_ph.empty()
		button2_ph.empty()
		button3_ph.empty()
		st.rerun()
