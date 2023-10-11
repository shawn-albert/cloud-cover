# Cloud Cover AI Chatbot

![Python 3.11](https://img.shields.io/badge/Python-3.11-blue.svg)
![AutoGen](https://img.shields.io/badge/AutoGen-<version>-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-<version>-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

## Overview

This repository houses a chatbot application engineered using the AutoGen library for backend logic and the Streamlit library for the frontend interface. The project demonstrates how a multi-agent conversation framework can be integrated with a Python web framework to create interactive applications.

## Project Description

The chatbot application is structured to facilitate easy development, testing, and deployment through Docker containers. The backend, powered by AutoGen, hosts the logic for agent interactions, while the frontend, designed with Streamlit, provides an interactive user interface for real-time conversations with the chatbot agent.

## To-Do List

- [ ] Implement additional agents for diverse conversation scenarios.
- [ ] Integrate a database for persistent storage of conversation history.
- [ ] Enhance the frontend design for a more engaging user experience.
- [ ] Add more comprehensive tests to ensure robustness.
- [ ] Explore deployment options for production readiness.

## Repository Structure

```plaintext
- project_directory/
    - backend/
        - agents/
            - chat_agent.py
        - Dockerfile
    - frontend/
        - assets/
            - icons/
                - user_icon.png
                - agent_icon.png
        - components/
            - ChatHistory.py
            - TextInput.py
        - styles/
            - ChatHistory.css
            - TextInput.css
        - app.py
        - Dockerfile
    - tests/
        - test_chat_agent.py
        - test_chat_interface.py
    - docker-compose.yml
    - pyproject.toml
    - main.py
```

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the dependencies using Poetry: `poetry install`
4. Build the Docker images: `docker-compose build`
5. Launch the application: `docker-compose up`

## Contributing Authors

- Shawn C. Albert
```
