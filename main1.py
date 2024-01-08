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
    start_time = st.time_input("Anfangszeit:")
    end_time = st.time_input("Endzeit:")
    user_email_id = st.text_input("Benutzer E-Mail-Adresse (ID):")
    
    if st.button("Reservierung anlegen/entfernen"):
        start_datetime = datetime.combine(reservation_date, start_time)
        end_datetime = datetime.combine(reservation_date, end_time)
        
        reservation_data = {
            "device_id": device_name,
            "start_datetime": start_datetime,
            "end_datetime": end_datetime,
            "user_email_id": user_email_id,
            # Weitere Reservierungsattribute hier hinzufügen
        }
        # Dosomething
        with st.spinner("Loading..."):
            time.sleep(1)
        st.success(f"Reservierung für {device_name} am {reservation_date} von {start_time} bis {end_time} für Benutzer {user_email_id} wurde angelegt/entfernt!")


# Wartung-Tab
elif selected_tab == "Wartung":
    if st.button("Wartungsinformationen anzeigen/aktualisieren"):
        with st.spinner("Loading..."):
            time.sleep(1)

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
        
        

# Anzeige des MCI-Logos in der Sidebar
st.sidebar.markdown("Quelle MCI-Logo: https://www.mci.edu/de/medien/logos-bilder")
