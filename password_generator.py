import random
import string
from fckin_colors import prRed, prCyan, prGreen



def password_generator(len_pass):
    letters_options = string.ascii_letters
    number_options =string.digits
    punctuation_options = string.punctuation
    options = letters_options + punctuation_options + number_options
    
    password = ""
    i=0
    while i <= len_pass:
        digit = random.choice(options)
        password += digit
        i+=1
    return prCyan(password)


choice_user = input("de quantos digitos será a sua senha? ")

while choice_user != "":
    if choice_user.isdigit():
        choice =int(choice_user)
        print(password_generator(choice))
        quit()
    else:
        prRed("oh oh! você precisa digitar um número")
        choice_user = input("de quantos digitos será a sua senha? ")
else:
    prGreen("lhe darei uma senha com 8 digitos então!") 
    print(password_generator(8))
