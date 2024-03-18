with open ("example.txt") as f1:
    games = f1.readlines()
with open ("games.txt") as f1:
    BigGames = f1.readlines()
print(games)
def getGame(games):
    def findBiggestGame(onecolorgames):
        numbers = []
        numberdic = {"maxnumber":0}
        for i in range(0,100):
            numbers.append(f'{i}')
        print(onecolorgames)
        for element in onecolorgames:
            count = ""
            for i in element:
                if i in numbers:
                    count+=i

            if int(count)>numberdic.get("maxnumber"):
                numberdic.update({"maxnumber":int(count)})

        return(numberdic.get("maxnumber"))
    import re
    idCombined = 0

    for i in games:
        pieces = re.findall("\d+\s+blue|\d+\s+red|\d+\s+green",i)
        print(pieces)

        redgames = re.findall("\d+\s+red",i)
        bluegames = re.findall("\d+\s+blue",i)
        greengames = re.findall("\d+\s+green",i)

        redmax = findBiggestGame(redgames)
        bluemax = findBiggestGame(bluegames)
        greenmax = findBiggestGame(greengames)

        idCombined+= (redmax*bluemax*greenmax)
        print(idCombined)
        #if there are no instances where there are too many any type balls this continues

getGame(games)
getGame(BigGames)