import tkinter as tk
from openai.api_client import APIClient

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("OpenAI Chatbot")
        self.geometry("400x600")

        self.api_client = APIClient()

        self.chat_history = tk.Text(self, state='disabled')
        self.chat_history.pack()

        self.entry = tk.Entry(self)
        self.entry.bind("<Return>", self.send_message)
        self.entry.pack()

    def send_message(self, event):
        message = self.entry.get()
        self.entry.delete(0, tk.END)

        self.append_to_chat("You: " + message)

        response = self.api_client.get_response(message)
        self.append_to_chat("Bot: " + response)

    def append_to_chat(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, message + "\n")
        self.chat_history.configure(state='disabled')