import streamlit as st
import random

# design
st.title("🎮 Rock Paper Scissors Game")

# options
options = ["rock", "paper", "scissors"]

# user choice
choice = st.selectbox("Choose Rock, Paper, or Scissors:", options)

# play button
if st.button("Play"):
    com = random.choice(options)

    st.write(f"Computer Choice: {com}")
    if choice == com:
        st.info("It it a tie")
    elif (
        (choice == "rock" and com == "scissors")
        or (choice == "paper" and com == "rock")
        or (choice == "scissors" and com == "paper")
    ):
        st.success("🎉 You Win!")
    else:
        st.error("💻 Computer Wins")
