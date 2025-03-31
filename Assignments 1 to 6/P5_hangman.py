import streamlit as st
import random

# Word list
words = ["python", "streamlit", "hangman", "developer", "coding"]

# Initialize session state
if "word" not in st.session_state:
    st.session_state.word = random.choice(words)
    st.session_state.display = ["_" for _ in st.session_state.word]
    st.session_state.guessed = set()
    st.session_state.attempts = 6

st.title("📝 Hangman Game")

# Display current state
st.write("Word: ", " ".join(st.session_state.display))

# User input
guess = st.text_input("Guess a letter:", max_chars=1).lower()

if st.button("Submit Guess") and guess:
    if guess in st.session_state.guessed:
        st.warning("You already guessed that letter!")
    else:
        st.session_state.guessed.add(guess)
        if guess in st.session_state.word:
            for idx, letter in enumerate(st.session_state.word):
                if letter == guess:
                    st.session_state.display[idx] = guess
        else:
            st.session_state.attempts -= 1

# Check win/loss
if "_" not in st.session_state.display:
    st.success("🎉 Congratulations! You guessed the word!")
    st.session_state.word = random.choice(words)
    st.session_state.display = ["_" for _ in st.session_state.word]
    st.session_state.guessed = set()
    st.session_state.attempts = 6
elif st.session_state.attempts == 0:
    st.error(f"😞 Game Over! The word was '{st.session_state.word}'.")
    st.session_state.word = random.choice(words)
    st.session_state.display = ["_" for _ in st.session_state.word]
    st.session_state.guessed = set()
    st.session_state.attempts = 6

st.write(f"Attempts left: {st.session_state.attempts}")
