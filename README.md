# OpenAI-Chatbot

This repository contains a simple Python-based UI interface that uses the OpenAI API to answer questions.

## Project Structure

The project is divided into several files and directories:

- `main.py`: This is the entry point of the application. It creates and starts the main window of the UI.
- `/ui`: This directory contains the `main_window.py` file, which defines the `MainWindow` class. This class represents the main window of the UI and handles user input and output.
- `/openai`: This directory contains the `api_client.py` file, which defines the `APIClient` class. This class is responsible for communicating with the OpenAI API.

## How to Run

To run the chatbot, you need to have Python and Tkinter installed. If you don't have them installed, you can download Python from the [official Python website](https://www.python.org/downloads/) and Tkinter is included with Python.

You also need to install the `openai` Python package. You can install it by running `pip install openai` in your terminal.

Once you have Python, Tkinter, and `openai` installed, you can run the chatbot by following these steps:

1. Open Terminal.
2. Navigate to the directory where the `main.py` file is located.
3. Run the program by typing `python main.py`.

Please note that you need to replace `'your-api-key'` in `api_client.py` with your actual OpenAI API key.

## How to Use

When you run the chatbot, a window will open. You can type your question into the text box at the bottom of the window and press Enter to send it. The chatbot's response will appear in the chat history above.