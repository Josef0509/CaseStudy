import streamlit as st
from datetime import datetime
import time
from st_pages import add_page_title

add_page_title()

# Wartungsinformationen anzeigen
if st.button("Wartungsinformationen anzeigen/aktualisieren"):
        
        with st.spinner("Loading..."):
            time.sleep(1)
            #Laden der Daten

        # Fiktive Wartungsdaten
        next_maintenance_dates = {"Gerät 1": datetime(2024, 4, 1), "Gerät 2": datetime(2024, 5, 15), "Gerät 3": datetime(2024, 6, 30)}
        
        # Anzeige der nächsten Wartungstermine
        st.subheader("Nächste Wartungstermine:")
        for device, next_maintenance_date in next_maintenance_dates.items():
            st.write(f"{device}: {next_maintenance_date.strftime('%Y-%m-%d')}")
        
        # Fiktive Wartungskosten pro Quartal
        maintenance_costs_per_quarter = {"Q1": 1500, "Q2": 1800, "Q3": 2000, "Q4": 1700}
        
        # Anzeige der Wartungskosten pro Quartal
        st.subheader("Wartungskosten pro Quartal:")
        for quarter, cost in maintenance_costs_per_quarter.items():
            st.write(f"{quarter}: {cost} Euro")

        st.success("Wartungsinformationen wurden angezeigt!")
        # Dosomething