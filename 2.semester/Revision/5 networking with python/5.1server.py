import socket
import threading
import pickle

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

address = 8080

HOST = ""

server.bind((HOST,address))
leaderboard = {}
def Handling_the_clients(connection,client_address):
    print(f"connected by {client_address}")
    questions = [{"What is the capital of Lithuania?":[{"A":"Vilnius"},{"B":"Riga"},{"C":"Helsinki"}]},
                 {"what is 1+1?":[{"A":"3"},{"B":"14"},{"C":"2"}]},
                 {"How much does an elephant weigh?":[{"A":"Plenty"},{"B":"A shit ton"},{"C":"2kg"}]}]
    answers = [1,3,2]
    #signing in and keeping track of the players
    clients = []




    connection.sendall(b"How many questions do you want to answer?")
    response = connection.recv(1024).decode() #a number sent by the client
    #print(type(int(response)))
    if type(int(response)) == int:
        connection.sendall("good".encode("UTF-8"))
        print("starting game")
        nrQuestions = 0 + int(response)
        index = 0
        score = 0
        while nrQuestions > 0 :
            question = pickle.dumps(questions[index],-1)
            connection.sendall(question)
            messagge = connection.recv(1024)
            messagge = messagge.decode()
            question = pickle.loads(question)
            for element in question:
                for answers in question.get(element):
                    #print(answers)
                    if answers.get(messagge):
                        score +=1
            nrQuestions -=1
            index+=1
            if index == len(questions):
                index = 0
        connection.sendall(f"You got {score} points".encode("UTF-8"))
    print(f"player {client_address} finished the game")

    connection.close()




while True:
    server.listen()
    connection, client_address = server.accept()
    T1 = threading.Thread(target=Handling_the_clients,args=(connection,client_address))
    T1.start()
