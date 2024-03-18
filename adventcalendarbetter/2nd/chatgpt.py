import re
with open("example.txt") as f1:
    games = f1.readlines()

allowedGreen = 13
allowedBlue = 14
allowedRed = 12


def IsGame(pieces):
    game = []
    for i in pieces:
        count, color = re.match(r"(\d+)\s+(blue|red|green)", i).groups()
        count = int(count)

        if color == "blue" and count > allowedBlue:
            game.append(False)
        elif color == "red" and count > allowedRed:
            game.append(False)
        elif color == "green" and count > allowedGreen:
            game.append(False)

    return game


def getGame(games):
    idCombined = ""
    for i in games:
        pieces = re.findall("\d+\s+(blue|red|green)", i)
        game = IsGame(pieces)
        if False not in game:
            idGame = re.findall("Game\s\d+", i)
            if idGame:
                idCombined += idGame[-1][-1]  # Extract the last character from the found Game ID

    print(f'combined id number is {idCombined}')


getGame(games)
