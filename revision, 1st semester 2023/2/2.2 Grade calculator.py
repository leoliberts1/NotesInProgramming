def Gradecalculator():
    Score = int(input("Enter score "))
    Grade = 'Grade is : '
    if Score > 90:
        return f'{Grade}A'
    elif Score > 80:
        return f'{Grade}B'
    elif Score > 70:
        return f'{Grade}C'
    elif Score > 60:
        return f'{Grade}D'
    return f'{Grade}F'

print(Gradecalculator())