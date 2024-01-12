import streamlit as st

from datetime import datetime
import time
from st_pages import add_page_title
from devices import Device
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

dateformat = "%Y-%m-%d "

person_data = {
	"name": ["Person 1", "Person 2", "Person 3"],
}

if st.session_state.show_session == 0:
	header_ph.header("Neues Gerät anlegen")
	device_name = device_ph.text_input("Name des Geräts:")
	article_number = article_number_ph.text_input("Artikelnummer:")
	acquisition_date = datetime.now().strftime(dateformat)
	change_date = datetime.now().strftime(dateformat)
	device_description = description_ph.text_area("Optionale Beschreibung:")
	device_responsible = responsible_person_ph.selectbox("verantwortliche Person:", person_data["name"])

	if button1_ph.button("Gerät anlegen/ändern"):
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
	devices = queries.find_devices()
	device_name = device_ph.selectbox("Gerät:", devices, placeholder="Gerät auswählen ...")

	device_data = Device.load_data_by_device_name(device_name)
	device_data.article_number = article_number_ph.text_input("Artikelnummer:", value = device_data.article_number)
	acquisition_date_ph.text(device_data.acquisition_date)
	device_data.change_date = datetime.now().strftime(dateformat)
	device_data.device_description = description_ph.text_area("Optionale Beschreibung:", value = device_data.device_description)
	device_data.managed_by_user_id = responsible_person_ph.selectbox("verantwortliche Person:", person_data["name"], index = person_data["name"].index(device_data.managed_by_user_id))
	#
	
	if button1_ph.button("Gerät ändern"):
		device_data.store_data()

		with st.spinner("Loading..."):
			time.sleep(1)
			#Save the device
   
		st.success(f"Gerät {device_data.device_name} mit dem Verantwortlichen {device_data.managed_by_user_id} wurde aktualisiert!")
		time.sleep(2)
		st.session_state.show_session = 0
		st.rerun()

	if button2_ph.button("Zurück"):
		st.session_state.show_session = 0
		st.rerun()

if st.session_state.show_session == 2:
	header_ph.header("Geräte anzeigen")
	devices = queries.find_devices()
	list_of_tabs = st.tabs(devices)

	for i in range(len(list_of_tabs)):
		with list_of_tabs[i]:
			device_data = Device.load_data_by_device_name(devices[i])

			st.title(device_data.device_name)
			st.text("ID: " + device_data.article_number)
			st.text("Verantwortliche Person: " + device_data.managed_by_user_id)
			st.text("letzte Änderung: " + device_data.change_date)
			st.text("Anschaffungsdatum: " + device_data.acquisition_date)

	if button1_ph.button("Zurück"):
		st.session_state.show_session = 0
		st.rerun()

import datetime
import time
from st_pages import add_page_title

add_page_title()

st.header("Neues Gerät anlegen oder bestehendes Gerät ändern")
device_name = st.text_input("Name des Geräts:")
article_number = st.text_input("Artikelnummer:")
acquisition_date = st.date_input("Anschaffungsdatum:")
device_description = st.text_area("Optionale Beschreibung:")
device_responsible = st.selectbox("verantwortliche Person:", ["Person 1", "Person 2", "Person 3"])

if st.button("Gerät anlegen/ändern"):
    device_data = {
        "name": device_name,
        "responsible_person": device_responsible,
        "__creation_date": datetime.datetime.now(),
        "article_number": article_number,
        "acquisition_date": acquisition_date,
        "description": device_description
        # Weitere Attribute hier hinzufügen
    }#dosomething

    with st.spinner("Loading..."):
            time.sleep(1)
            #Save the gerät

    st.success(f"Gerät {device_name} mit dem Verantwortlichen {device_responsible} wurde angelegt/aktualisiert!")

