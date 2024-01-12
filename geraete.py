import streamlit as st

from datetime import datetime
import time
from st_pages import add_page_title
import sys

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

#Fake data
device_data = {
	"name": ["Gerät 1", "Gerät 2", "Gerät 3", "Gerät 4"],
	"responsible_person": ["Person 1", "Person 2", "Person 3", "Person 2"],
	"__creation_date": [datetime(2021, 1, 1), datetime(2022, 3, 13), datetime(2020, 6, 30), datetime(2023, 10, 4)],
	"article_number": ["123456", "234567", "345678", "456789"],
	"acquisition_date": [datetime(2021, 1, 1), datetime(2022, 3, 13), datetime(2020, 6, 30), datetime(2023, 10, 4)],
	"description": ["Dies ist ein Testgerät", "Dies ist ein Testgerät", "Dies ist ein Testgerät", "Dies ist ein Testgerät"]
	# Weitere Attribute hier hinzufügen
}

person_data = {
	"name": ["Person 1", "Person 2", "Person 3"],
}

if st.session_state.show_session == 0:
	header_ph.header("Neues Gerät anlegen")
	device_name = device_ph.text_input("Name des Geräts:")
	article_number = article_number_ph.text_input("Artikelnummer:")
	acquisition_date = acquisition_date_ph.date_input("Anschaffungsdatum:")
	device_description = description_ph.text_area("Optionale Beschreibung:")
	device_responsible = responsible_person_ph.selectbox("verantwortliche Person:", person_data["name"])

	if button1_ph.button("Gerät anlegen/ändern"):
		device_data = {
			"name": device_name,
			"responsible_person": device_responsible,
			"__creation_date": datetime.now(),
			"article_number": article_number,
			"acquisition_date": acquisition_date,
			"description": device_description
			# Weitere Attribute hier hinzufügen
		}

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
	device_name = device_ph.selectbox("Gerät:", device_data["name"], placeholder="Gerät auswählen ...")

	if device_name in device_data["name"]:
		device_responsible = device_data["responsible_person"][device_data["name"].index(device_name)]
		device_article_number = device_data["article_number"][device_data["name"].index(device_name)]
		device_acquisition_date = device_data["acquisition_date"][device_data["name"].index(device_name)]
		device_description = device_data["description"][device_data["name"].index(device_name)]

		device_article_number = article_number_ph.text_input("Artikelnummer:", value = device_article_number)
		device_acquisition_date = acquisition_date_ph.date_input("Anschaffungsdatum:", value= device_acquisition_date)
		device_description = description_ph.text_area("Optionale Beschreibung:", value = device_description)
		device_responsible = responsible_person_ph.selectbox("verantwortliche Person:", device_data["responsible_person"], index = device_data["responsible_person"].index(device_responsible))

		if button1_ph.button("Gerät ändern"):
			device_data["article_number"][device_data["name"].index(device_name)] = device_article_number
			device_data["acquisition_date"][device_data["name"].index(device_name)] = device_acquisition_date
			device_data["description"][device_data["name"].index(device_name)] = device_description
			device_data["responsible_person"][device_data["name"].index(device_name)] = device_responsible

			with st.spinner("Loading..."):
				time.sleep(1)
				#Save the device

			st.success(f"Gerät {device_name} mit dem Verantwortlichen {device_responsible} wurde aktualisiert!")
			time.sleep(2)
			st.session_state.show_session = 0
			st.rerun()

	if button2_ph.button("Zurück"):
		st.session_state.show_session = 0
		st.rerun()

if st.session_state.show_session == 2:
	header_ph.header("Geräte anzeigen")
	list_of_tabs = st.tabs(device_data["name"])

	for i in range(len(list_of_tabs)):
		with list_of_tabs[i]:

			st.title(device_data["name"][i])
			st.text("ID: " + str(i))
			st.text("Verantwortliche Person: " + device_data["responsible_person"][i])
			st.text("letzte Änderung: " + str(device_data["__creation_date"][i]))
			st.text("Anschaffungsdatum: " + str(device_data["acquisition_date"][i]))

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

