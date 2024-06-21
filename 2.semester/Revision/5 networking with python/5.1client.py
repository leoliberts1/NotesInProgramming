import socket,pickle

HOST = "localhost"

PORT = 8080

def playing_game(socket,nrQuestions):
    for i in range(nrQuestions):
        msg = socket.recv(1024)
        msg = pickle.loads(msg)
        #print(msg)
        for element in msg:
            print(element)
            for answers in msg.get(element):
                print(answers)
        response  = input("Enter your answer here")
        socket.sendall(response.encode("UTF-8"))
    msg = socket.recv(1024).decode()
    print(msg)
    socket.close()


with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    data = s.recv(1024) # we recieve the question of how many
    #questions we want to answer
    nrQuestions = int(input(data.decode("UTF-8")))
    messagge = str(nrQuestions)
    s.sendall(messagge.encode("UTF-8"))
    if s.recv(1024).decode() == "good":
        playing_game(s,nrQuestions)
    else:
        print("restart program")
