
def where_to(command_str):
    command_str = list(command_str)
    x = 0
    y = 0
    for command in command_str:
        if command == "↑":
            y+=1
        elif command == "↓":
            y = y-1
        elif command == "→":
            x += 1
        elif command == "←":
            x = x-1
    return print(x,y)

#where_to("↑→→→↑←←←↑↑→→→↑←←←←←←←←↑→↓↓↓→↓↑↑↑↑→↓↓↓→↓↑↑↑←←←←←←←←←←←←←←←←←←→→→↑↑→↓↓↓→↓↓↑→→→↑↑→↓↓↑↓↓↑→→→↑→→→↑↑→↓↓↓↑↑→↓↓↓↑↑↑→↓↓↓→→↑↑↓↓↓")
# should return (1,1)




def happynumbers(n):
    happy = []
    start = 1
    number_now = 0
    #while len(happy)<n:



##############
def find_winners(file,winningnum):
    import re
    with open(file) as f :
        data = f.readlines()
    print(data)
    #good_data = {}
    #for person in data:
        #good_data.update({(re.findall("\d\d\d+",person)):re.findall("\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+",person)})
    #print(good_data)
    good_data = {}
    for person in data:
        personalid = re.findall(r"\d\d\d+",person)
        #print(personalid)
        #print(person)
        personalnum = re.findall(r"\d+,\s\d+,\s\d+,\s\d+,\s\d+,\s\d+",person)
        #print(personalnum)
        numbers = ""
        chosen_num = []
        for element in personalnum:
            element = element +" "
            for letter in element:
                #print(letter)
                if letter in ['1','2','3','4','5','6','7','8','9','0'] :
                    numbers = numbers+letter
                else :
                    if len(numbers) !=0:
                        chosen_num.append(int(numbers))
                        numbers = ''
                    else:continue
        #print(chosen_num)
        good_data.update({int(personalid[0]):chosen_num})
    winners = []
    for person1 in good_data:
        #print(person1)
        if good_data.get(person1) == winningnum:
            winners.append(person1)
    return winners



print(find_winners("lotto-players.txt",[45, 23, 31, 13, 36, 17]))


