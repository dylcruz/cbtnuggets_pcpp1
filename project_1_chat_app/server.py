import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.clients = []
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()


    def start_server(self):
        print('Server is now listening for connections.')

    def stop_server(self):
        print('Stopping server.')

    def handle_client(self, client_socket):
        pass

    def broadcast_message(self, message, source_client):
        pass

if __name__ == '__main__':
    server = ChatServer('0.0.0.0', 8000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()