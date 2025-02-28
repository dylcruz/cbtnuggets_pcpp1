import socket
import pickle

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 8000
hands = ['rock', 'paper', 'scissors']

try:
    client_socket.connect((host, port))

    while True:
        hand = input('Please enter rock, paper, or scissors: ')
        if hand not in hands:
            print(f'Invalid choice.')
        else:
            break
    
    hand_data = pickle.dumps(hand)

    client_socket.sendall(hand_data)

    response_data = client_socket.recv(1024)
    response = pickle.loads(response_data)
    print(response)

except ConnectionResetError:
    print('Could not connect to the server!')

client_socket.close()
