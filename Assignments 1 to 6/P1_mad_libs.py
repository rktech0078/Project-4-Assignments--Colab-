import streamlit as st
import random

st.set_page_config(page_title="Mad Libs Game", page_icon="🎭")

story = [
    "One day, the {noun} decided to {verb} and it became very {adjective}!",
    "The {noun} always {verb}s when it feels {adjective}.",
    "If you are {adjective}, you should {verb} with a {noun}!",
    "Once upon a time, a {adjective} {noun} wanted to {verb} all day long.",
    "Never trust a {adjective} {noun} when it tries to {verb}!"
]


st.title("Mad Libs Game 🎭")

noun = st.text_input("Enter a noun (person, place, or thing)")
verb = st.text_input("Enter a verb (action word)")
adjective = st.text_input("Enter an adjective (describing word)")

if st.button("Generate Story"):
    
    if noun and verb and adjective:
        story = random.choice(story).format(noun=noun, verb=verb, adjective=adjective)
        st.success(f"Your story is: \n{story}")
    else:
        st.warning("⚠️ Please fill in all the fields!")