import socket 
import threading 

PORT = 8000
ADDRESS = "0.0.0.0"

broadcast_list = []

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_socket.bind((ADDRESS, PORT))


def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print("Client removed: {}".format(client))

def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            print("Received message: {}".format(message))
            broadcast(message)
        else:
            print("client has been disconnected: {}".format(client))
            return

def start_listen_thread(client):
    client_thread = threading.Thread(target=listen_thread, args=(client,))
    client_thread.start()

def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listen_thread(client)

accept_loop()
