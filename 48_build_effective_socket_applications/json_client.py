import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

person = { 'name': 'Dylan', 'age': 29, 'hair_color': 'black'}

try:
    client_socket.connect((host, port))
    person_data = pickle.dumps(person)
    client_socket.sendall(person_data)
    response = client_socket.recv(1024).decode('utf-8')
    print(f'The server says {response}')
except ConnectionResetError:
    print('Could not connect to the server!')

