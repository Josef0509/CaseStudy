from st_pages import Page, add_page_title, show_pages
import streamlit as st

add_page_title()

def load_other_script(name_file):
    with open(name_file) as f:
        code = compile(f.read(), name_file, "exec")
        exec(code, globals(), locals())
        
show_other_file = False

if not show_other_file:
    load_other_script("geraete.py")
    if st.button('Andere Datei anzeigen'):
        show_other_file = True
else:
    load_other_script("geraete_anzeigen.py")
    if st.button('Andere Datei verstecken'):
        show_other_file = False
    