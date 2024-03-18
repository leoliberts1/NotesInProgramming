def countStrongPasswords(filename):
    with open(filename) as f:
        text = f.readlines()
    passwords = []
    num_passwords = 0
    for var in text:
        var = var.replace("\n", "")
        if var[0].isdigit() :
            continue
        #num_lower = 0
        num_Upper = 0
        num_underscore = 0
        for letter in var:
            #if letter.islower() == True:
                #num_lower += 1
            if letter.isupper()== True:
                num_Upper += 1
            if letter == "_":
                num_underscore+=1
        if num_underscore < 1 or num_Upper < 2:
            continue
        if var[0].islower() == True:
            if var[-1].islower() != True:
                continue
        passwords.append(var)
        num_passwords += 1

    return passwords, num_passwords


# Test your code
print(countStrongPasswords("passwords-examples-txt"))