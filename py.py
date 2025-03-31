import streamlit as st
import random

st.title("🎮 Guess the Number Game!")

# User selects the mode
mode = st.radio("Select Game Mode:", ["User vs Computer", "Computer vs User"])

if mode == "User vs Computer":
    st.subheader("🔢 User Guessing Mode")
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.number_input("Apna guess likhein (1-100):", min_value=1, max_value=100, step=1)
    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess < st.session_state.secret_number:
            st.warning("Zyada bara sochiye! 🔼")
        elif guess > st.session_state.secret_number:
            st.warning("Zyada chhota sochiye! 🔽")
        else:
            st.success(f"🎉 Mubarak ho! Aapne {st.session_state.attempts} attempts me sahi number guess kiya! 🎯")
            st.session_state.secret_number = random.randint(1, 100)
            st.session_state.attempts = 0

elif mode == "Computer vs User":
    st.subheader("🤖 Computer Guessing Mode")
    if "low" not in st.session_state:
        st.session_state.low, st.session_state.high = 1, 100
        st.session_state.computer_attempts = 0
        st.session_state.computer_guess = random.randint(st.session_state.low, st.session_state.high)

    st.write(f"Computer ka guess: **{st.session_state.computer_guess}**")
    
    feedback = st.radio("Yeh number:", ["Bara hai", "Chhota hai", "Sahi hai"], index=2)

    if st.button("Next Guess"):
        st.session_state.computer_attempts += 1
        if feedback == "Bara hai":
            st.session_state.high = st.session_state.computer_guess - 1
        elif feedback == "Chhota hai":
            st.session_state.low = st.session_state.computer_guess + 1
        else:
            st.success(f"🎉 Computer ne {st.session_state.computer_attempts} attempts me sahi number guess kar liya! 🤖")
            st.session_state.low, st.session_state.high = 1, 100
            st.session_state.computer_attempts = 0

        st.session_state.computer_guess = random.randint(st.session_state.low, st.session_state.high)
