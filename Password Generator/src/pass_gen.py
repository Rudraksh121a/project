import random
import string

def password_generator(min_length,number=True,special_charcater=True):
    
    letters=string.ascii_letters
    digit=string.digits
    special=string.punctuation

    charactor=letters

    if number:
        charactor += digit
    if special_charcater:
        charactor += special
    
    

    password=""
    meet_criteria=False
    has_number=False
    has_special=False



    while not meet_criteria or len(password) < min_length:
        new_char=random.choice(charactor)
        password += new_char

        if new_char in digit:
            has_number = True
        elif new_char in special:
            has_special=True

        meet_criteria=True
        if number:
            meet_criteria=has_number
        if special_charcater:
            meet_criteria= meet_criteria and has_special

    
    return password

