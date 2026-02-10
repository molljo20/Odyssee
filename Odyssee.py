import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="Odysseus Irrfahrt", layout="wide")

st.title("🌊 Die Irrfahrt des Odysseus")
st.write("Du bist Odysseus! Reise von **Troja** zurück nach **Ithaka**.")

stations = [
    {
        "name": "Troja",
        "coords": (39.957, 26.238),
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Troy_sunset.jpg",
        "info": "Troja ist der Ausgangspunkt von Odysseus’ Heimreise. "
                "Nach dem Trojanischen Krieg beginnt seine lange Irrfahrt. "
                "Die Götter stellen sich ihm in den Weg. "
                "Viele Abenteuer und Gefahren warten. "
                "Hier startet die Odyssee."
    },
    {
        "name": "Land der Zyklopen",
        "coords": (37.6, 15.1),
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0b/Polyphemus_Ulysses.jpg",
        "info": "Odysseus trifft auf Polyphem, den Zyklopen. "
                "Er frisst einige seiner Männer. "
                "Odysseus blendet ihn mit List. "
                "So kann er entkommen. "
                "Doch Poseidon wird sein Feind."
    },
    {
        "name": "Kirke",
        "coords": (41.25, 13.1),
        "image": "https://upload.wikimedia.org/wikipedia/commons/5/5a/Circe_John_William_Waterhouse.jpg",
        "info": "Kirke ist eine mächtige Zauberin. "
                "Sie verwandelt Männer in Tiere. "
                "Odysseus widersteht ihrer Magie. "
                "Sie hilft ihm schließlich weiter. "
                "Er bleibt ein Jahr auf ihrer Insel."
    },
    {
        "name": "Die Sirenen",
        "coords": (40.55, 14.25),
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3f/Sirens_playing.jpg",
        "info": "Die Sirenen singen tödlich schön. "
                "Odysseus will sie hören. "
                "Er lässt sich an den Mast binden. "
                "Seine Männer hören nichts wegen Wachs. "
                "So überleben sie."
    },
    {
        "name": "Ithaka",
        "coords": (38.4, 20.7),
        "image": "https://upload.wikimedia.org/wikipedia/commons/3/3d/Ithaca_Greece.jpg",
        "info": "Odysseus erreicht endlich Ithaka. "
                "Doch sein Palast ist besetzt. "
                "Er kämpft um sein Zuhause. "
                "Er besiegt die Freier. "
                "Die Reise endet siegreich."
    },
]

if "current" not in st.session_state:
    st.session_state.current = 0

current_station = stations[st.session_state.current]

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🗺️ Karte der Reise")

    m = folium.Map(location=current_station["coords"], zoom_start=5)

    for i, station in enumerate(stations):

        if i == st.session_state.current:
            # 🔴 Roter Kreis für Odysseus
            folium.CircleMarker(
                location=station["coords"],
                radius=15,
                color="red",
                fill=True,
                fill_color="red",
                popup=f"🌟 Odysseus ist hier: {station['name']}"
            ).add_to(m)

            # Kleines Text-Label „Odysseus“ über den Kreis
            folium.map.Marker(
                station["coords"],
                icon=folium.DivIcon(
                    html=f"""<div style="font-size:10px; color:white; font-weight:bold; text-align:center;">Odysseus</div>"""
                )
            ).add_to(m)

        else:
            folium.Marker(
                location=station["coords"],
                popup=station["name"],
                icon=folium.Icon(color="blue")
            ).add_to(m)

    st_folium(m, width=700, height=500)

with col2:
    st.subheader(f"📍 Aktuelle Station: {current_station['name']}")
    st.image(current_station["image"], use_container_width=True)

    if st.button("ℹ️ Was passiert hier?"):
        st.info(current_station["info"])

    st.write("---")

    if st.session_state.current < len(stations) - 1:
        if st.button("⛵ Reise zur nächsten Station"):
            st.session_state.current += 1
            st.rerun()
    else:
        st.success("🎉 Odysseus ist endlich in Ithaka angekommen!")
