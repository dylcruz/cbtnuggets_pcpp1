import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

print(f'Waiting for connections on {host}:{port}')

server_socket.bind((host, port))
server_socket.listen(3)

client_socket, client_address = server_socket.accept()
print(f'A new client has connected, with address {client_address}')

# Listen for message, and respond to client

while True:
    data = client_socket.recv(1024).decode('utf-8')

    print(f'The client says: {data}')
    client_socket.sendall(f'I received your message: {data}'.encode('utf-8'))
    
    if data == 'done':
        break

client_socket.close()
