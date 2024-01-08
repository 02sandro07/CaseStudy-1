import streamlit as st
from datetime import datetime
import time

# Diese Bild soll rechts angezeigt werden
st.sidebar.image('MCI.png', width=300)
st.sidebar.title("Hochschulgeräteverwaltung")

# Verschiedene Tab Typen

selected_tab = st.sidebar.selectbox("Navigation", ["Geräte", "Nutzer", "Reservierungen", "Wartung"])

# Geräte-Tab
if selected_tab == "Geräte":
    
    st.header("Neues Gerät anlegen oder bestehendes Gerät ändern")
    
    # Eingabefelder für Geräteinformationen
    device_name = st.text_input("Name des Geräts:")
    article_number = st.text_input("Artikelnummer:")
    acquisition_date = st.date_input("Anschaffungsdatum:")
    device_description = st.text_area("Optionale Beschreibung:")
    
    if st.button("Gerät anlegen/ändern"):
        device_data = {
            "name": device_name,
            "article_number": article_number,
            "acquisition_date": acquisition_date,
            "description": device_description,
            "__creation_date": datetime.now(),
            # Weitere Attribute hier hinzufügen
        }
        # Dosomething
        with st.spinner("Loading..."):
            time.sleep(1)
        st.success(f"Gerät {device_name} mit Artikelnummer {article_number} wurde angelegt/aktualisiert!")


# Nutzer-Tab
elif selected_tab == "Nutzer":
    st.header("Neuen Nutzer anlegen")
    user_email = st.text_input("E-Mail-Adresse des Nutzers:")
    user_name = st.text_input("Name des Nutzers:")
    
    if st.button("Nutzer anlegen"):
        # Dosomething
        with st.spinner("Loading..."):
            time.sleep(1)
        st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")


# Reservierungen-Tab
elif selected_tab == "Reservierungen":
    st.header("Reservierung anlegen oder entfernen")
    
    # Erstelle ein Dropdown-Menü mit allen Geräten
    device_name = st.selectbox("Gerät:", ["Gerät 1", "Gerät 2", "Gerät 3"])
    
    # Eingabefelder für Reservierungsinformationen
    reservation_date = st.date_input("Reservierungsdatum:")
    reservation_time = st.time_input("Reservierungszeit:")
    user_email_id = st.text_input("Benutzer E-Mail-Adresse (ID):")
    
    if st.button("Reservierung anlegen/entfernen"):
        reservation_data = {
            "device_id": device_name,
            "reservation_date": datetime.combine(reservation_date, reservation_time),
            "user_email_id": user_email_id,
            # Weitere Reservierungsattribute hier hinzufügen
        }
        # Dosomething
        with st.spinner("Loading..."):
            time.sleep(1)
        st.success(f"Reservierung für {device_name} am {reservation_date} um {reservation_time} für Benutzer {user_email_id} wurde angelegt/entfernt!")


# Wartung-Tab
elif selected_tab == "Wartung":
    st.header("Wartungsinformationen")
    
    if st.button("Wartungsinformationen anzeigen"):
        # Dosomething
        with st.spinner("Loading..."):
            time.sleep(1)
        st.success("Wartungsinformationen wurden angezeigt!")

# Anzeige des MCI-Logos in der Sidebar
st.sidebar.markdown("Quelle MCI-Logo: https://www.mci.edu/de/medien/logos-bilder")
