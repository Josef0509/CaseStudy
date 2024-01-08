import streamlit as st
import datetime
from st_pages import add_page_title

add_page_title()

st.header("Neues Gerät anlegen oder bestehendes Gerät ändern")
device_name = st.text_input("Name des Geräts:")
device_responsible = st.text_input("Verantwortliche Person:")
if st.button("Gerät anlegen/ändern"):
    device_data = {
        "name": device_name,
        "responsible_person": device_responsible,
        "__creation_date": datetime.now(),
        # Weitere Attribute hier hinzufügen
    }#dosomething
    st.success(f"Gerät {device_name} mit dem Verantwortlichen {device_responsible} wurde angelegt/aktualisiert!")