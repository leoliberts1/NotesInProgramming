from TicTacToe import Tictactoe
import socket
import pickle
#First set up the server and get both of the clients to connect
#make sure that both of them get a message notifying them
#their either first or second


s = socket.socket()

HOST = ""
PORT = 8000

s.bind((HOST,PORT))

s.listen(1)

conn1,addr1 = s.accept()
print("connection1 made")
conn2,addr2 = s.accept()
print("connection2 made")
message1 = conn1.recv(1024).decode()
print("Player 1",message1)
message2 = conn2.recv(1024).decode()
print("Player 2",message2)
game = Tictactoe(message1,message2)

while not game.gameWon()[0]:
    board = game.getBoardTxt()
    try:
        print(game.turn(), end=" ")
        #choice = int(input(">> "))
        if game.turn() == message1:
            conn1.send(pickle.dumps([board,"chose where to place your shit"],-1))
            conn2.send(pickle.dumps([board]))
            choice = pickle.loads(conn1.recv(1024))
        else:
            conn1.send(pickle.dumps([board]))
            conn2.send(pickle.dumps([board,"chose where to place your shit"],-1))
            choice = pickle.loads(conn2.recv(1024))
    except:
        print("please enter a valid field")
        conn1.send(pickle.dumps("please enter a valid field"))
        conn2.send(pickle.dumps("please enter a valid field"))
        continue
    if game.board[choice - 1] == 'X' or game.board[choice - 1] == 'O':
        print("illegal move, plase try again")
        conn1.send(pickle.dumps("illegal move, plase try again"))
        conn2.send(pickle.dumps("illegal move, plase try again"))
        continue

    game.makeMove(choice)
    end, winner = game.gameWon()
    if end:
        print(game.getBoardTxt())
        print("Player " + str(winner) + " wins!\n")
        conn1.send(pickle.dumps([f"Player {winner} wins!\n"]))
        conn2.send(pickle.dumps([f"Player {winner} wins!\n"]))
        conn1.send(pickle.dumps(["exit"]))
        conn2.send(pickle.dumps(["exit"]))
conn1.close()
conn2.close()
s.close()
