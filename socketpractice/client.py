import socket

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name and port number
host = socket.gethostname()
port = 9999

# connect to the server
client_socket.connect((host, port))

# read input from standard input and send to server
message = input("Enter a message: ")
client_socket.send(message.encode())

# receive the modified message from server and print
modified_message = client_socket.recv(1024).decode()
print("Modified message received from server: " + modified_message)

# close the socket
client_socket.close()
