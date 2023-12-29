import streamlit as st
from datetime import datetime

# Diese bild soll rechts angezeigt werden
st.sidebar.image('MCI.png', width=300)
st.sidebar.title("Hochschulgeräteverwaltung")

# Erstelle die Tabs in der Sidebar
selected_tab = st.sidebar.radio("Navigation", ["Geräte", "Nutzer", "Reservierungen", "Wartung"])

# Geräte-Tab
if selected_tab == "Geräte":
    #st.image('MCI.png', width=400, caption='MCI Logo: https://www.mci.edu/de/medien/logos-bilder')
    st.header("Neues Gerät anlegen oder bestehendes Gerät ändern")
    device_name = st.text_input("Name des Geräts:")
    device_responsible = st.text_input("Verantwortliche Person:")
    if st.button("Gerät anlegen/ändern"):
        device_data = {
            "name": device_name,
            "responsible_person": device_responsible,
            "__creation_date": datetime.now(),
            # Weitere Attribute hier hinzufügen
        }
        # dosomething
        st.success(f"Gerät {device_name} mit dem Verantwortlichen {device_responsible} wurde angelegt/aktualisiert!")

# Nutzer-Tab
elif selected_tab == "Nutzer":
    #st.image('MCI.png', width=400, caption='MCI Logo: https://www.mci.edu/de/medien/logos-bilder')

    st.header("Neuen Nutzer anlegen")
    user_email = st.text_input("E-Mail-Adresse des Nutzers:")
    user_name = st.text_input("Name des Nutzers:")
    if st.button("Nutzer anlegen"):
        # dosomething
        st.success(f"Nutzer {user_name} ({user_email}) wurde angelegt!")

# Reservierungen-Tab
elif selected_tab == "Reservierungen":
    #st.image('MCI.png', width=400, caption='MCI Logo: https://www.mci.edu/de/medien/logos-bilder')

    st.header("Reservierung anlegen oder entfernen")
    # Erstelle ein Dropdown-Menü mit allen Geräten
    device_name = st.selectbox("Gerät:", ["Gerät 1", "Gerät 2", "Gerät 3"])
    reservation_date = st.date_input("Reservierungsdatum:")
    if st.button("Reservierung anlegen/entfernen"):
        reservation_data = {
            "device_id": device_name,
            "reservation_date": reservation_date,
            # Weitere Reservierungsattribute hier hinzufügen
        }
        # dosomething
        st.success(f"Reservierung für {device_name} wurde für den {reservation_date} angelegt/entfernt!")

# Wartung-Tab
elif selected_tab == "Wartung":
    # Anzeige des MCI-Logos in der Hauptseite
    #st.image('MCI.png', width=400, caption='MCI Logo: https://www.mci.edu/de/medien/logos-bilder')

    st.header("Wartungsinformationen")
    if st.button("Wartungsinformationen anzeigen"):
        # dosomething
        st.success("Wartungsinformationen wurden angezeigt!")


#st.sidebar.text("Quelle MCI-Logo: https://www.mci.edu/de/medien/logos-bilder") 
#st.sidebar._text_input("Quelle MCI-Logo: https://www.mci.edu/de/medien/logos-bilder")
st.sidebar.markdown("Quelle MCI-Logo: https://www.mci.edu/de/medien/logos-bilder")

