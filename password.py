import string

password = input("enter your password : ")
lower ,upper,digit,latter,punctuation = 0,0,0,0,0

if len(password) >= 8:
    for i in password:
        if i.islower():
            lower += 10
        if i.upper():
            upper += 10
        if i.isdigit():
            digit += 10
        if i in string.punctuation:
            punctuation += 5
        if i.isalpha():
            latter += 10
if lower >= 10 and upper >= 10 and digit >= 10 and latter >= 10 and punctuation >= 5:
    print("valid password ..")
else:
    print("try anther password that contain at least 8 char ,  contain lower and upper char , at least one digit and punctuation sign.")






























