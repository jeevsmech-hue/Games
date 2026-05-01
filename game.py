import streamlit as st
import random

st.set_page_config(page_title="DJ's Number Guessing Game", page_icon="🎯")
st.title("🎯 Number Guessing Game")
st.write("I'm thinking of a number between **1 and 100**!")

# Initialize session state
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 100)
if "attempts_left" not in st.session_state:
    st.session_state.attempts_left = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "won" not in st.session_state:
    st.session_state.won = False
if "started" not in st.session_state:
    st.session_state.started = False

# Difficulty selection
if not st.session_state.started:
    difficulty = st.radio("Choose difficulty:", ["Easy (10 attempts)", "Hard (5 attempts)"])
    if st.button("Start Game"):
        st.session_state.attempts_left = 10 if "Easy" in difficulty else 5
        st.session_state.started = True
        st.rerun()

else:
    st.info(f"Attempts remaining: {st.session_state.attempts_left}")

    if not st.session_state.game_over:
        guess = st.number_input("Make a guess:", min_value=1, max_value=100, step=1)

        if st.button("Guess!"):
            if guess < st.session_state.number:
                st.warning("📉 Too low! Try higher.")
            elif guess > st.session_state.number:
                st.warning("📈 Too high! Try lower.")
            else:
                st.session_state.won = True
                st.session_state.game_over = True
                st.rerun()

            st.session_state.attempts_left -= 1
            if st.session_state.attempts_left == 0 and not st.session_state.won:
                st.session_state.game_over = True
                st.rerun()

    if st.session_state.game_over:
        if st.session_state.won:
            st.success("🎉 You got it right!")
        else:
            st.error(f"💀 Game Over! The number was {st.session_state.number}")

        if st.button("Play Again"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()
