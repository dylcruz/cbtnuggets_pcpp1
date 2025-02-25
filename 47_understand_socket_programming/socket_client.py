import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

client_socket.connect((host, port))

# Send message to server

while True:
    next_message = input('Please enter the next message you want to to send the server: ')
    client_socket.sendall(next_message.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(f'The server responded with: {data}')
    if next_message == 'done':
        break

client_socket.close()
