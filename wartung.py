import streamlit as st
import datetime
from st_pages import add_page_title

add_page_title()

# Wartungsinformationen anzeigen
st.header("Wartungsinformationen")
if st.button("Wartungsinformationen anzeigen/aktualisieren"):
    
       
    st.success("Wartungsinformationen wurden angezeigt!")
    # Dosomething