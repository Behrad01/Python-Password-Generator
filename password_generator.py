import string
import random

# defining password_generator function
def generate_password(length):
    # validating user input ( length )
    try:
        length = int(length)
    except ValueError:
        raise ValueError('Length must be a number.')
    
    if length <= 0:
        raise ValueError('Length must be greater than 0')

    # a list of characters including numbers and letters
    characters = string.ascii_letters + string.digits + string.punctuation   
    password = ''  

    # creating a random password with specified length
    for _ in range(length):
        password += random.choice(characters) 

    # defining variables that help with creating formatted password
    num_of_dashes = length // 4   # calculating number of dashes 
    target_indices = [index * 4 for index in range(1, num_of_dashes + 1)]   # dash string indices

    # creating formatted password (with dashes)
    formatted_password = '' 
    for index, name in enumerate(password, 1):
        formatted_password += name

        # putting a dash if string index matches target index
        if index in target_indices and index != length:
            formatted_password += '-'

    return formatted_password   # returning formatted password   

if __name__ == '__main__':
    user_input = input('Enter password length: ')   # catching user input
    print(generate_password(user_input))   # generating password with generate_password function
