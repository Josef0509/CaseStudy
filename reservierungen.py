import streamlit as st
import time
from st_pages import add_page_title

add_page_title()

st.header("Reservierung anlegen oder entfernen")
#creating a dropdown menu with all devices
device_name = st.selectbox("Gerät:", ["Gerät 1", "Gerät 2", "Gerät 3"])
reserver = st.selectbox("Reservierende Person:", ["Person 1", "Person 2", "Person 3"])
reservation_date = st.date_input("Reservierungsdatum:")
start_time = st.time_input("Anfangszeit:")
end_time = st.time_input("Endzeit:")
if st.button("Reservierung anlegen/entfernen"):
    reservation_data = {
        "device_id": device_name,
        "reservation_date": reservation_date,
        "reserver": reserver,
        "start_time": start_time,
        "end_time": end_time
        # Weitere Reservierungsattribute hier hinzufügen
    }#dosomething

    with st.spinner("Loading..."):
            time.sleep(1)
            #Save the data
            
    st.success(f"Reservierung von {device_name} wurde für {reserver} am {reservation_date} von {start_time} bis {end_time} angelegt/entfernt!")