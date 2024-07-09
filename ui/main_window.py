import tkinter as tk
from tkinter import scrolledtext
from openai.api_client import APIClient

class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("OpenAI Chatbot")
        self.geometry("400x600")

        self.api_client = APIClient()

        # Using scrolledtext for chat history to include a scrollbar
        self.chat_history = scrolledtext.ScrolledText(self, state='disabled', wrap=tk.WORD)
        self.chat_history.pack(padx=10, pady=10)

        self.entry = tk.Entry(self)
        self.entry.bind("<Return>", self.send_message)
        self.entry.pack(padx=10, pady=10)

    def send_message(self, event):
        """Send the message to OpenAI API and display the response."""
        message = self.entry.get()
        self.entry.delete(0, tk.END)
        self.insert_message(message, "You")
        try:
            response = self.api_client.query(message)
            self.insert_message(response, "Bot")
        except Exception as e:
            self.insert_message("Failed to get response from API.", "Error")

    def insert_message(self, message, sender):
        """Inserts a message into the chat history."""
        self.chat_history.config(state='normal')
        self.chat_history.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_history.config(state='disabled')
        # Auto-scroll to the bottom
        self.chat_history.yview(tk.END)

if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()