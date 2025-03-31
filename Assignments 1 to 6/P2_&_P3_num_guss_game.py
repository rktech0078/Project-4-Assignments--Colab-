import streamlit as st 
import random

st.title("Number Guessing Game")

mode = st.radio("Select Mode: ", ["USER  vs  COMPUTER","COMPUTER  vs  USER"])

st.write("---")

if mode == "USER  vs  COMPUTER":
    st.subheader("🔢 User Guessing Mode")
    
    secret = st.session_state.get("secret", random.randint(1,5))
    attempts = st.session_state.get("attempts", 0)
    
    user_guess = st.number_input("Select a number between (1-5)",  min_value=1, max_value=5, step=1)
    
    if st.button("Submit"):
        attempts += 1
        if user_guess < secret:
            st.error("Think bigger! 🔼")
        elif user_guess > secret:
            st.error("Think smaller! 🔽")
        else:
            st.success(f"🎉 Correct! You guessed in {attempts} attempts!")
            secret, attempts = random.randint(1,5), 0
            
        st.session_state["secret"], st.session_state["attempts"] = secret, attempts
        
else:
    st.subheader("🤖 Computer Guessing Mode")
    
    low, high = st.session_state.get("low", 1), st.session_state.get("high", 100)
    attempts = st.session_state.get("comp_guess", 0)
    computer_guess = random.randint(low, high)
    
    st.info(f"The Guess of Computer is: {computer_guess}")
    
    human_feedback = st.radio("Hey Computer, Guess: ", ["TOO HIGH", "TOO LOW", "CORRECT"])
    
    if st.button("Next Guess"):
        attempts += 1
        if human_feedback == "TOO HIGH":
            high = computer_guess + 1
        elif human_feedback == "TOO LOW":
            low = computer_guess - 1
        else:
            st.success(f"🎉 Computer guessed it in {attempts} attempts!")
    
    low, high, attempts = 1 , 100 , 0
    
    st.session_state.update({
        "low": low,
        "high": high,
        "comp_guess": attempts
    })
            