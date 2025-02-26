import socket
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8001

client_socket.connect((host, port))



# Send message to server

def start_input_loop():
    while True:
        next_message = input('Please enter the next message you want to to send the server: ')
        client_socket.sendall(next_message.encode('utf-8'))
        data = client_socket.recv(1024).decode('utf-8')
        if next_message == 'done':
            break

    client_socket.close()

input_loop = threading.Thread(target=start_input_loop)
input_loop.start()

def listen_for_messages():
    while True:
        data = client_socket.recv(1024).decode('utf-8')
        print(f'\nNew Message!: {data}')

messages_loop = threading.Thread(target=listen_for_messages)
messages_loop.start()