import socket
while True:
    client_socket, address = s.accept()
    t1 = threading.Thread(target=handle_client,args=(address, client_socket))
    t1.start()
client_socket.close()
def handle_client (address, socket):
## Your code to handle the client