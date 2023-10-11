# ChatHistory.py
import streamlit as st

def render_chat_history(chat_history: list) -> None:
    """Renders the chat history in the Streamlit app.

    Args:
        chat_history (list): A list of tuples representing the chat history.
    """
    for msg in chat_history:
        if msg[0] == 'User':
            st.markdown(f"**{msg[0]}**: {msg[1]}")
        else:
            st.markdown(f"_{msg[0]}_: {msg[1]}")
