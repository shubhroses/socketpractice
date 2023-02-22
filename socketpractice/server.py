import socket

# create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name and port number
host = socket.gethostname()
port = 9999

# bind the socket to a specific port
server_socket.bind((host, port))

# listen for incoming connections
server_socket.listen(1)

# wait for a client to connect
print("Waiting for a client to connect...")
client_socket, client_address = server_socket.accept()
print("Client connected: " + str(client_address))

# receive message from client and convert to uppercase
message = client_socket.recv(1024).decode()
modified_message = message.upper()

# send the modified message back to the client
client_socket.send(modified_message.encode())

# close the sockets
client_socket.close()
server_socket.close()
