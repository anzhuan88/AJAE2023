
import streamlit as st
import random
import os

AL_IMAGES = [
    "AJAE.png",
    "Al-playing-saxo-01-by-dominiquechappard.svg",
    "paro-AL-calling.svg",
    "paro-AL-jumping.svg",
    "paro-AL-sleeping.svg",
    "paro-Al-sliding-on-a-banana-skin.svg",
    "263006.png",
    "283821.png",
]



def show_al_stickman(randomize=True, width=150):
    filename = random.choice(AL_IMAGES) if randomize else AL_IMAGES[0]
    image_path = os.path.join("assets", filename)

    # Streamlit can display SVG when given as a file path
    st.sidebar.image(image_path, width=width)



