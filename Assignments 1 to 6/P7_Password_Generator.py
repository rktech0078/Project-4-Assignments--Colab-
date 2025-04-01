import streamlit as st
import random
import string

def generated_password(length, use_special, use_digit):
    
    character = string.ascii_letters
    
    if use_digit:
        character += string.digits
        
    if use_special:
        character += string.punctuation
        
    result = "".join(random.choice(character) for _ in range(length))
    
    return result


st.title("🔐 Generate Password")

length = st.slider("Password Length", min_value=6, max_value=12, value=8)
use_digit = st.checkbox("Include Digits")
use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password", use_container_width=True):
    result = generated_password(length, use_special, use_digit)
    st.write("Your Generated Passcode is: ")
    st.code(result)