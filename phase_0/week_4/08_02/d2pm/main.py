import streamlit as st
from PIL import Image

img = Image.open('warnet.jpg')

st.image(img, caption='lumba-lumba warnet')