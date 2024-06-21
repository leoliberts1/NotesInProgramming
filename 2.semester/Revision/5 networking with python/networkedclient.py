import socket

s = socket.socket()

host  = socket.gethostname()

port = 8080

s.connect((host,port))
print("connected to server")

message = s.recv(1024)
message.decode()
print("server message ",message)
while True:
    message = s.recv(1024)
    message = message.decode()
    print("Server :",message)
    new_message = input(str(">>"))
    s.send(new_message.encode())
