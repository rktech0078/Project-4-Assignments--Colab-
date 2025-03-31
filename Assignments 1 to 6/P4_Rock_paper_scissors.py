import streamlit as st
import random

st.title("Rock, Paper, Scissor")

choices = ["Rock","Paper","Scissor"]

user_choice = st.radio("Choose One: ", choices)

computer_choice = random.choice(choices)

if st.button("Play"):
    st.info(f"Computer choice is: **{computer_choice}**")
    
    if user_choice == computer_choice:
        st.warning("Its a Tie")
    elif (
        (user_choice == "Rock" and computer_choice == "Scissor") or
        (user_choice == "Scissor" and computer_choice == "Paper") or
        (user_choice == "Paper" and computer_choice == "Rock")
    ) :
        st.success(f"You're winner because you choose: **{user_choice}**")
    
    else:
        st.error("Computer Win")