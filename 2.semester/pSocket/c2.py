import socket
# Connecting to a local server
#print(b"sviests?")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8000))
msg = b""
while msg.decode("utf-8") !="bye":
    msg = b"Hi Server" # can also use .encode('utf-8')
    msg = input("write whatever you want to send to the server ").encode("utf-8")
    s.sendall(msg)

    message_from_server = s.recv(4096)

    print(message_from_server.decode("utf-8"))
s.close()