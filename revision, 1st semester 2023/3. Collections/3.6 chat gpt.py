Example1 = ["XO_XXXOO_"]
Example2 = ['XOOOXXOXO']
Example3 = ["X_X_XOOOX"]

def WhoWon(Game):
    for i in range(3):  # Loop for rows
        if Game[0][i * 3] == Game[0][i * 3 + 1] == Game[0][i * 3 + 2] and Game[0][i * 3] in ["O", "X"]:
            print(f"Game won by {Game[0][i * 3]}")
            return

    for i in range(3):  # Loop for columns
        if Game[0][i] == Game[0][i + 3] == Game[0][i + 6] and Game[0][i] in ["O", "X"]:
            print(f"Game won by {Game[0][i]}")
            return

    if Game[0][0] == Game[0][4] == Game[0][8] and Game[0][0] in ["O", "X"]:  # Diagonal from top-left to bottom-right
        print(f"Game won by {Game[0][0]}")
        return

    if Game[0][2] == Game[0][4] == Game[0][6] and Game[0][2] in ["O", "X"]:  # Diagonal from top-right to bottom-left
        print(f"Game won by {Game[0][2]}")
        return

    print("No one has won the game.")


WhoWon(Example1)
WhoWon(Example2)
WhoWon(Example3)
