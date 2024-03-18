
def check(limit):
    def ispalindromic(arg):
        arg = list(str(arg))
        if arg == arg[::-1]:
            return True
        else:
            return False
    squares = []
    for i in range(1,limit+1):
        if i*i <limit+1:
            squares.append(i*i)
    print(squares)
    index_start = 0
    numbers = []
    while index_start < len(squares):
        number = 0
        for index in range(index_start,len(squares)):
            if number == 0:
                number = squares[index]
                continue
            else:
                number+=squares[index]
                if ispalindromic(number) and number < limit+1:
                    numbers.append(number)
        index_start+=1
    return sorted(numbers)

print(len(check(98765)))