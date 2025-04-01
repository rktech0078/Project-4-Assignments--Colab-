import streamlit as st
import random

words: list = ["python", "streamlit", "hangman", "developer", "coding"]

if "state" not in st.session_state:
    word = random.choice(words)
    st.session_state.state = {
        "word": word,
        "display": ["_"] * len(word),
        "guessed": set(),
        "attempts": 6
    }
    
game = st.session_state.state

st.title("📝 HANGMAN GAME")

st.write("Words: ", " ".join(game["display"]))

user_guess = st.text_input("Guess a letter: ", max_chars=1).lower()

if st.button("Submit") and user_guess:
    if user_guess in game["guessed"]:
        st.warning('Letter is already guessed')
    else:
        game['guessed'].add(user_guess)
        if user_guess in game['word']:
            game['display'] = [user_guess if c == user_guess else d for c, d in zip(game['word'], game['display'])]
        else:
            game['attempts'] -= 1
            

if "_" not in game["display"]:
    st.success("YOU WIN")
    st.session_state.state = None or st.write("Game Over! Try Again")
    
st.write(f"Attempts Left: {game["attempts"]}")