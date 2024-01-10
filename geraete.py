import streamlit as st
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