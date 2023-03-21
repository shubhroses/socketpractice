import socket
import numpy as np

# create a socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name and port number
host = "174.129.92.182"
port = 9999

# connect to the server
client_socket.connect((host, port))

# create a numpy array and send it to server
arr = np.array([1, 2, 3, 4, 5], dtype=np.int32)
client_socket.send(arr.tobytes())

# receive the modified array from server and print
modified_arr_bytes = client_socket.recv(1024)
modified_arr = np.frombuffer(modified_arr_bytes, dtype=np.int32)
print("Modified array received from server: " + str(modified_arr))

# close the socket
client_socket.close()

