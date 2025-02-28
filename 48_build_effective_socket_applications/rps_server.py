import socket
import pickle

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 8000

server_socket.bind((host, port))
server_socket.listen(3)

print(f'Server up on {host}:{port}. Waiting for connections...')

client_socket_1, client_address_1 = server_socket.accept()
print(f'Client 1 at {client_address_1} has connected.')

client_socket_2, client_address_2 = server_socket.accept()
print(f'Client 2 at {client_address_2} has connected.')

client_1_data = client_socket_1.recv(1024)
client_1_hand = pickle.loads(client_1_data)

client_2_data = client_socket_2.recv(1024)
client_2_hand = pickle.loads(client_2_data)

intro_message = f'Client 1 chooses {client_1_hand}. Client 2 chooses {client_2_hand}.'
print(intro_message)

if client_1_hand == client_2_hand:
    win_message = 'Tie!'

elif client_1_hand == 'rock' and client_2_hand == 'scissors':
    win_message = 'Client 1 wins!'

elif client_1_hand == 'scissors' and client_2_hand == 'paper':
    win_message = 'Client 1 wins!'

elif client_1_hand == 'paper' and client_2_hand == 'rock':
    win_message = 'Client 1 wins!'

else:
    win_message = 'Client 2 wins!'

print(win_message)
result_data = pickle.dumps(f'{intro_message} {win_message}')
client_socket_1.sendall(result_data)
client_socket_2.sendall(result_data)

client_socket_1.close()
client_socket_2.close()
