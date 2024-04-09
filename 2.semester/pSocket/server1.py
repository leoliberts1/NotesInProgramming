import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",8000))
s.listen()

client_socket, address = s.accept()
while True:
    print("A client from address",address,"has just connected")

    message_from_client = client_socket.recv(1024)

    print("Got the message from client : ",message_from_client.decode("utf-8"))
    message_from_client = message_from_client.decode("utf-8")
    if message_from_client == "bye":
        break
    client_socket.sendall((b"Hello in return!"))


client_socket.close()