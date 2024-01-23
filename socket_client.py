import socket  # Importing the socket module to create network sockets

# Defining the host and port to connect to
HOST = 'example-service-name-yyrg.onrender.com'  # Localhost IP address
PORT = '443'  # Port number to connect to

data = f'''POST https://{HOST}/gimme:{PORT}/ HTTPS/1.1
Host: {HOST}:{PORT}
Content-Length: 20
Content-Type: application/json
Accept-Encoding: gzip, deflate, compress
Accept: */*
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36

{'{"helow": "roworor"}'} '''


# Creating a socket object for the client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connecting to the server at the specified host and port
client_socket.connect((HOST, int(PORT)))

# Sending a message to the server by encoding a string to bytes using UTF-8 encoding and sending it through the socket
client_socket.send(data.encode('utf-8'))

# Receiving a response from the server by receiving up to 1024 bytes of data through the socket and decoding it to a string using UTF-8 encoding
print(client_socket.recv(1024))

# Closing the socket connection with the server
client_socket.close()
