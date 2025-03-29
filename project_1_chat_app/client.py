import socket
import threading
from tkinter import *
from tkinter import scrolledtext

class ChatClient:
    def __init__(self, host, port):
        self.window = Tk()
        self.window.title("Chat Application")

        self.chat_area = scrolledtext.ScrolledText(self.window, state='disabled', wrap=WORD)
        self.chat_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.new_message_entry = Entry(self.window)
        self.new_message_entry.grid(row=1, column=0, padx=10, pady=10, sticky='ew')

        self.send_button = Button(self.window, text='Send', command=self.send_message)
        self.send_button.grid(row=1, column=1, padx=10, pady=10, sticky='ew')

        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((host, port))

    def run(self):
        receive_thread = threading.Thread(target=self.receive_messages)
        receive_thread.daemon = True
        receive_thread.start()

        self.window.protocol('WM_DELETE_WINDOW', self.on_closing)
        mainloop()

    def send_message(self):
        message = self.new_message_entry.get()

        if message:
            self.client_socket.send(message.encode('utf-8'))
            self.new_message_entry.delete(0, END)
            self.display_message(message, own_message=True)

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('UTF-8')
                if message:
                    self.display_message(message)
            except OSError:
                break

    def display_message(self, message, own_message=False):
        self.chat_area.config(state='normal')
        if own_message:
            self.chat_area.insert(END, 'You: ' + message + '\n')
        else:
            self.chat_area.insert(END, message + '\n')
        self.chat_area.config(state='disabled')
        self.chat_area.yview(END)

    def on_closing(self):
        self.window.destroy()

if __name__ == '__main__':
    client = ChatClient('0.0.0.0', 8000)
    client.run()
