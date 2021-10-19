import random
print('Welcome to Password Generator')
lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
UPPERCASE = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']


passwordlength = int(input("Enter password length:-\n")) 
passwordstrength = input("Strength:-\n" "(1)Low\n" "(2)Medium\n" "(3)Strong\n" "Enter the strength:- ")
passwordcount = int(input("Numbers of password you want to generate:-\n"))

for x in range(0,passwordcount):

    
    if passwordstrength == "Low":
        password1 = []
        password1.extend((lowercase))
        random.shuffle(password1)
        print("Your password is:- ")
        print("".join(password1[0:passwordlength]))
    elif passwordstrength == "Medium":
        password2 = []
        password2.extend(lowercase)
        password2.extend(UPPERCASE)
        password2.extend(numbers)
        random.shuffle(password2)
        print("Your password is:- ")
        print("".join(password2[0:passwordlength]))
    
    elif passwordstrength == "Strong":
        password3 = []
        password3.extend(lowercase)
        password3.extend(UPPERCASE)
        password3.extend(numbers)
        password3.extend(special)
        random.shuffle(password3)
        print("Your password is:- ")
        print("".join(password3[0:passwordlength]))


