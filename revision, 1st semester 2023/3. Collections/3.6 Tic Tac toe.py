Example1 = ["XO_XXXOO_"]
Example2 = ['XOOOXXOXO']
Example3 = ["X_X_XOOOX"]

def WhoWon (Game):
    for i in range(0,3):
        #Check first if the rows are the same
        if Game[0][i*3] == Game[0][i*3+1] == Game[0][i*3+2]:
            #find out who won
            if Game[0][i*3] == "O":
                print("Game won by O")
                return
            elif Game[0][i*3] == "X":
                print("Game won by X")
                return
        #Check if the colums are the same
        elif Game[0][i] == Game[0][i+3] == Game[0][i+6]:
            if Game[0][i*3] == "O":
                print("Game won by O")
                return
            elif Game[0][i*3] == "X":
                print("Game won by X")
                return
        #Check diagonal from left up to right down
        elif Game[0][0] == Game[0][4] == Game[0][8]:
            if Game[0][0] == "O":
                print("Game won by O")
                return
            elif Game[0][0] == "X":
                print("Game won by X")
                return
        elif Game[0][3] == Game[0][4] == Game[0][6]:
            if Game[0][0] == "O":
                print("Game won by O")
                return
            elif Game[0][0] == "X":
                print("Game won by X")
                return
    print("No one won")
    return


WhoWon(Example1)
WhoWon(Example2)
WhoWon(Example3)