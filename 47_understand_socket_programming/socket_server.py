import socket
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clients = []

host = socket.gethostname()
port = 8001

print(f'Waiting for connections on {host}:{port}')

server_socket.bind((host, port))
server_socket.listen(3)

def handle_client(client_socket):
    global clients
    
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f'The client says: {data}')        
        for client in clients:
            client.sendall(data.encode('utf-8'))

        if data == 'done':
            break
    
    client_socket.close()
    clients.remove(client_socket)

while True:
    client_socket, client_address = server_socket.accept()
    clients.append(client_socket)
    print(f'A new client has connected, with address {client_address}')
    new_thread = threading.Thread(target=handle_client, args=(client_socket,))
    new_thread.start()
