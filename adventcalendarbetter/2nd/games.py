


with open ("example.txt") as f1:
    games = f1.readlines()
with open ("games.txt") as f1:
    BigGames = f1.readlines()
print(games)
def IsGame(pieces):
    allowedGreen = 13
    allowedBlue = 14
    allowedRed = 12
    game = []
    print(pieces)
    for i in pieces:
        print(i)
        print(i[3])
        if i[3] == "b":
            if int(i[0]+i[1])>allowedBlue:
                game.append("False")
        elif i[3] == "r":
            if int(i[0]+i[1])>allowedRed:
                game.append("False")
        elif i[3] == "g":
            if int(i[0]+i[1])>allowedGreen:
                game.append("False")
    print(game)
    return(game)
game1 = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green\n"
import re
def getGame(games):
    import re
    idCombined = 0

    for i in games:
        pieces = re.findall("\d+\s+blue|\d+\s+red|\d+\s+green",i)
        game = IsGame(pieces)
        print(game)
        #if there are no instances where there are too many any type balls this continues
        if "False" not in game:
            Gamenr = re.findall("Game\s\d+", i)
            print(Gamenr)
            gameid = Gamenr[0]
            print(len(gameid))
            #if the game number is from 0 to 9
            if len(gameid) == 6:
                number = int(gameid[-1])
                idCombined = idCombined+number
            #if the game number is from 10 to 99
            elif len(gameid) == 7:
                number = int(gameid[-2]+gameid[-1])
                idCombined = idCombined+number
            #if the game number is from 100 to 999
            elif len(gameid) == 8:
                number = int(gameid[-3]+gameid[-2]+gameid[-1])
                idCombined = idCombined +number







    return(print(f'combined id number is  {idCombined} '))


getGame(BigGames)

