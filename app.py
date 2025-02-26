import streamlit as st

st.title("🚀 Galactic Mad Libs 🌌")

# Collect inputs from the user
astronaut_name = st.text_input("🧑‍🚀Enter an astronaut's name:")
planet = st.text_input("🌍Enter a planet name (real or imaginary):")
alien_species = st.text_input("👽Enter an alien species (e.g. Zorgons, Fluffians):")
special_item = st.text_input("🔮🧪Enter a magical/science item (e.g. Quantum Crystal, Plasma Scepter):")

if st.button("Launch Story"):
    story = (
        f"Commander **{astronaut_name}** was preparing for the most dangerous mission of their career.\n\n"
        f"The goal? To retrieve the legendary **{special_item}** from the core of **{planet}**.\n\n"
        f"Suddenly, their spaceship was surrounded by **{alien_species}**! Just when all hope seemed lost...\n\n"
        f"Commander {astronaut_name} remembered the ancient prophecy about the **{special_item}**.\n\n"
        "With a daring maneuver and quick thinking, they activated the artifact's power,\n"
        f"creating a portal that transported them safely to **{planet}**'s surface.\n\n"
        "The universe would never be the same..."
    )
    st.write(story)