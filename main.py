import streamlit as st
from datetime import datetime

st.title("ABC")

#creating tabs
tab1, tab2, tab3, tab4 = st.tabs(["Geräte", "Nutzer", "Reservierungen", "Wartung"])

with tab1:
   # Gerät anlegen/ändern
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

with tab2:
   # Nutzer anlegen
   st.header("Neuen Nutzer anlegen")
   user_email = st.text_input("E-Mail-Adresse des Nutzers:")
   user_name = st.text_input("Name des Nutzers:")
   if st.button("Nutzer anlegen"):
      #dosomething
      st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")

with tab3:
   st.header("Reservierung anlegen oder entfernen")
   #creating a dropdown menu with all devices
   device_name = st.selectbox("Gerät:", ["Gerät 1", "Gerät 2", "Gerät 3"])
   reservation_date = st.date_input("Reservierungsdatum:")
   if st.button("Reservierung anlegen/entfernen"):
      reservation_data = {
         "device_id": device_name,
         "reservation_date": reservation_date,
         # Weitere Reservierungsattribute hier hinzufügen
      }#dosomething
      st.success(f"Reservierung für {device_name} wurde für den {reservation_date} angelegt/entfernt!")

with tab4:
   # Wartungsinformationen anzeigen
   st.header("Wartungsinformationen")
   if st.button("Wartungsinformationen anzeigen"):
      #dosomething
      st.success("Wartungsinformationen wurden angezeigt!")



