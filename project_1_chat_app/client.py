import socket
import threading
from tkinter import *

class ChatClient:
    def __init__(self, host, port):
        self.window = Tk()
        self.window.title("Chat Application")

        # UI Setup

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def run(self):
        pass

    def send_message(self):
        pass

    def receive_messages(self):
        pass

    def display_message(self):
        pass

    def on_closing(self):
        pass

if __name__ == '__main__':
    client = ChatClient('0.0.0.0', 8000)
    client.run()