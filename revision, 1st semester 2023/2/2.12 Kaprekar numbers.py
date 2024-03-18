def isKaprekar(ARG):
    def isSquareSame(Arg):
        arg1 = Arg
        arg2 = Arg*Arg
        if len(str(arg2)) > 1:
            for element in str(arg2):
                if str(arg2).index(element) == 0 :
                    start = int(element)
                    end = int(str(arg2)[1::])
                elif str(arg2).index(element) != len(str(arg2))-1 :
                    start = int(str(arg2)[0:str(arg2).index(element)+1])
                    end = int(str(arg2)[str(arg2).index(element)+1::])
                else:
                    start = int(str(arg2)[0:str(arg2).index(element)])
                    end = int(element)
                if arg1 == start+end:
                    return True
        return False
    if ARG > 0 and ARG == int(ARG):
        if isSquareSame(ARG):
            return(print(f'{ARG} Is a kaprekar number'))
        else: return(print(f'{ARG} Is not a Kaprekar number'))
isKaprekar(45)
for i in range(1,101):
    isKaprekar(i)