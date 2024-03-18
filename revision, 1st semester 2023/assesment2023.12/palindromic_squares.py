def palindromicSquares(n):
    def ispalindromic(arg):
        arg = list(arg)
        if arg == arg[::-1]:
            return True
        else: return False
    numbers = []
    start = 0
    while n > 0 :
        if ispalindromic(str(start)) == True and ispalindromic(str(start*start)) == True:
            numbers.append(start*start)
            n = n-1
        start+=1
    return(numbers)

# Example usage:
result = palindromicSquares(16)
print (result)
nothing = 1234
nothing = list(str(nothing))
print(nothing)