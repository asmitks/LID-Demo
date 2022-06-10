import streamlit as st
from alphabet_detector import AlphabetDetector
from PIL import Image
import time 
image = Image.open('koo.png')


col1, mid, col2 = st.columns([1,1,20])
with col1:
    st.image(image, width=60)
with col2:
    st.title('Demo for LID')
# keyboard = Controller()
ad = AlphabetDetector()

title = st.text_input('Enter String')
start = time.time()
det =ad.detect_alphabet(title)
end = time.time()
st.write(det)
st.write(f"Operation time : {end-start} seconds")
