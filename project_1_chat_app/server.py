import socket
import threading

class ChatServer:
    def __init__(self, host, port):
        self.clients = []
        self.client_id = 1
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()

    def start_server(self):
        print('Server is now listening for connections.')

        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append({'id': self.client_id, 'socket': client_socket})
            self.client_id += 1
            print(f'Client connected from {addr}')
            thread = threading.Thread(target=self.handle_client, args=(client_socket,))
            thread.start()

    def stop_server(self):
        print('Stopping server.')

    def handle_client(self, client_socket):
        while True:
            try:
                message_decode = client_socket.recv(1024).decode('UTF-8')                
                if not message_decode:
                    break
                message = f'Client {client_id}: {message_decode}'.encode('UTF-8')               
                self.broadcast_message(message, client_socket)
                
            except Exception as e:
                print(f'Exception: {e}')
                break

        self.clients.remove(client_socket)
        client_socket.close()

    def broadcast_message(self, message, source_client):
        for client in self.clients:
            if client is not source_client:
                try:
                    client.send(message)
                except Exception as e:
                    print(f'Exception when broadcasting: {e}')

if __name__ == '__main__':
    server = ChatServer('0.0.0.0', 8000)
    try:
        server.start_server()
    except KeyboardInterrupt:
        server.stop_server()
