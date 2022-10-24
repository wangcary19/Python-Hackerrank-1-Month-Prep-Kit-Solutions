def password_input():
    """
    INPUT: none.
    
    PROCESSING:
        Asks user to input password.
        Checks user input for length.
        Prompts re-entry if password is less than 8 characters.

    OUTPUT: returns password.
    """
    while True:
        password = input("Enter a password: ")
        if len(password) >= 8:
            break
        else:
            print("ERROR: Password too short!")
            continue
    return password

def uppercase_check(arg):
    """
    INPUT: string argument.
    
    PROCESSING:
        Uses a for loop to iterate over arg.
        Returns True if a character is uppercase.
        Otherwise returns False.
        
    OUTPUT: returns True or False.
    """
    for i in arg:
        if i.isupper():
            return True
        else:
            return False
