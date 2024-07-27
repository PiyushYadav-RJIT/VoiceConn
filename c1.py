import socket
import threading
import random

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode()
            print("\n", message)
        except:
            print("Disconnected from server.")
            break

def send_messages():
    print("Connected to server.")
    while True:
        message = input("")
        if message.strip():
            client_socket.send(message.encode())

HOST = '152.59.27.39'
PORT = 12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Generate a 5-digit random number for verification
client_id = str(random.randint(10000, 99999))

print("Connected to server. Your client ID is:", client_id)

# Ask the client to enter their name
client_name = input("Enter your name: ")
client_socket.send(client_name.encode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()
