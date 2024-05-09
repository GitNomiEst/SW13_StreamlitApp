import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(page_title="My Streamlit App")
st.header("Dokumente teilen")
st.write("Diese App ermöglicht dir Dokumente mit deinen Freunden zu teilen.")


@st.cache
def fetch_and_clean_data(url):
    # Fetch data from URL here, and then clean it up.
    return data

def main():
    # Texteingabefeld für den Benutzer
    user_input = st.text_area("Gib deinen Text ein:", height=200)

    # Teilt den Text mit anderen Benutzern
    shared_text = st.text_area("Gemeinsam bearbeitetes Dokument:", height=200)

    save_shared_text(shared_text)

def save_shared_text(text):
    # text speichern... with open("shared_text.txt", "w") as f:
    # f.write(text)
    pass

if __name__ == "__main__":
    main()
