def ThanosWouldbeProud():
    values = {}
    values = dict(values)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for element in alphabet:
        values.update({element:alphabet.index(element)+1})
    print(values)
    word = str(input("Enter a word "))
    if len(word)%2 !=0:
        first_half = word[0:len(word)//2]
        second_half = word[len(word)//2+1:]
        f_value,s_value = 0,0
        for letter in first_half:
            f_value+= values.get(letter)
        for letter in second_half:
            s_value += values.get(letter)
        print(f_value,s_value)
        if f_value == s_value:
            return f'{word} is balanced'
        else:return f'{word} is not balanced'
    else:
        first_half = word[0:int(len(word)/2)]
        second_half = word[int(len(word)/2):]
        f_value, s_value = 0, 0
        for letter in first_half:
            f_value+= values.get(letter)
        for letter in second_half:
            s_value += values.get(letter)
        print(f_value,s_value)
        if f_value == s_value:
            return f'{word} is balanced'
        else:return f'{word} is not balanced'
print(ThanosWouldbeProud())