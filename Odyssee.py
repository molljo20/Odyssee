import streamlit as st
import folium
from streamlit_folium import st_folium

# -----------------------------
# Seitentitel & Layout
# -----------------------------
st.set_page_config(page_title="Odysseus Irrfahrt", layout="wide")

st.title("🌊 Die Irrfahrt des Odysseus")
st.write(
    "Du bist Odysseus! Reise nach dem Trojanischen Krieg von **Troja** zurück nach **Ithaka**."
)

# -----------------------------
# Stationen der Odyssee
# -----------------------------
stations = [
    {
        "name": "Troja",
        "coords": (39.957, 26.238),
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Troy_sunset.jpg",
        "info": "Troja ist der Ausgangspunkt von Odysseus’ Heimreise nach dem Trojanischen Krieg. "
                "Nach zehn Jahren Kampf will er endlich zurück nach Ithaka. "
                "Doch die Götter sind ihm nicht wohlgesonnen. "
                "Seine Reise wird voller Gefahren und Prüfungen. "
                "Hier beginnt die berühmte Irrfahrt."
    },
    {
        "name": "Land der Zyklopen",
        "coords": (37.6, 15.1),
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Polyphemus_Ulysses.jpg",
        "info": "Odysseus trifft auf den Zyklopen Polyphem, einen riesigen einäugigen Riesen. "
                "Dieser verschlingt einige seiner Männer. "
                "Odysseus überlistet ihn mit dem Tricknamen 'Niemand'. "
                "Er blendet den Zyklopen und entkommt. "
                "Doch Polyphem ruft den Zorn Poseidons hervor."
    },
    {
        "name": "Kirke",
        "coords": (41.25, 13.1),
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Circe_John_William_Waterhouse.jpg",
        "info": "Die Zauberin Kirke lebt auf einer geheimnisvollen Insel. "
                "Sie verwandelt Odysseus’ Männer in Schweine. "
                "Mit Hilfe von Hermes kann Odysseus sie besiegen. "
                "Kirke wird schließlich zur Verbündeten. "
                "Sie gibt wichtige Hinweise für die Weiterreise."
    },
    {
        "name": "Die Sirenen",
        "coords": (40.55, 14.25),
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Sirens_playing.jpg",
        "info": "Die Sirenen locken Seeleute mit ihrem betörenden Gesang ins Verderben. "
                "Odysseus möchte sie hören, ohne zu sterben. "
                "Er lässt seine Männer Wachs in die Ohren stopfen. "
                "Sich selbst bindet er an den Mast des Schiffes. "
                "So entkommen sie dieser tödlichen Gefahr."
    },
    {
        "name": "Ithaka",
        "coords": (38.4, 20.7),
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Ithaca_Greece.jpg",
        "info": "Nach vielen Jahren erreicht Odysseus endlich Ithaka. "
                "Doch zuhause haben sich Freier in seinem Palast breitgemacht. "
                "Mit List und Mut kämpft er sich zurück auf den Thron. "
                "Er vereint sich wieder mit Penelope. "
                "Die lange Irrfahrt findet ihr Ende."
    },
]

# -----------------------------
# Fortschritt speichern
# -----------------------------
if "current" not in st.session_state:
    st.session_state.current = 0

current_station = stations[st.session_state.current]

# -----------------------------
# Layout: Karte links, Info rechts
# -----------------------------
col1, col2 = st.columns([2, 1])

# -----------------------------
# Karte anzeigen
# -----------------------------
with col1:
    st.subheader("🗺️ Karte der Reise")

    # Karte zentrieren auf aktuelle Station
    m = folium.Map(
        location=current_station["coords"],
        zoom_start=5
    )

    # Marker für alle Stationen
    for i, station in enumerate(stations):

        # Aktuelle Station: Odysseus als kleines Männchen
        if i == st.session_state.current:

            odysseus_icon = folium.CustomIcon(
                icon_image="https://cdn-icons-png.flaticon.com/512/4140/4140048.png",
                icon_size=(40, 40)
            )

            folium.Marker(
                location=station["coords"],
                popup=f"🧍 Odysseus ist hier: {station['name']}",
                icon=odysseus_icon
            ).add_to(m)

        # Andere Stationen: normale blaue Marker
        else:
            folium.Marker(
                location=station["coords"],
                popup=station["name"],
                icon=folium.Icon(color="blue")
            ).add_to(m)

    st_folium(m, width=700, height=500)

# -----------------------------
# Station Info + Bild
# -----------------------------
with col2:
    st.subheader(f"📍 Aktuelle Station: {current_station['name']}")

    st.image(current_station["image"], use_container_width=True)

    # Info-Button
    if st.button("ℹ️ Was passiert hier?"):
        st.info(current_station["info"])

    st.write("---")

    # Weiterreise Button
    if st.session_state.current < len(stations) - 1:
        if st.button("⛵ Reise zur nächsten Station"):
            st.session_state.current += 1
            st.rerun()
    else:
        st.success("🎉 Odysseus ist endlich in Ithaka angekommen!")
