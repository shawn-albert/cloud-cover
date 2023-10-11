# TextInput.py
import streamlit as st
from backend.agents.chat_agent import ChatAgent

def handle_text_input(chat_agent: ChatAgent, chat_history: list) -> list:
    """Handles user text input and agent response.

    Args:
        chat_agent (ChatAgent): The chat agent instance.
        chat_history (list): The chat history.

    Returns:
        list: Updated chat history.
    """
    user_input = st.text_input("Type your message...", key='user_input')
    if st.button("Send"):
        agent_response = chat_agent.on_message(user_input)
        chat_history.append(('User', user_input, False))
        chat_history.append(('Agent', agent_response, False))
    return chat_history
