import socket,pickle

HOST = "localhost"

PORT = 8000

s = socket.socket()

s.connect((HOST,PORT))

s.send(input("Write your username").encode())
Game = True

while Game:
    def trying():
        try:
            choice = int(input(message[1]))
            if choice > 0 and choice < 10 and choice != None:
                return choice
            else:
                print("please enter a valid field")
                trying()
        except:
            print("please enter a valid field")
            trying()
    message = pickle.loads(s.recv(1024))
    #print(message)
    if len(message)>1:
        print(message[0])
        choice = trying()
        s.send(pickle.dumps(choice))
    elif message == ["exit"]:
        Game = False
    else:
        print(message[0])
s.close()
print("game has finished")