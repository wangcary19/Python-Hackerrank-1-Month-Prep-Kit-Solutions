"""
Name: Hana Pak
Assignment: 6
Problem: 3
Partner: None
"""

#import statement
import passwordchecker

#defining functions
def lowercase_check(arg):
    for i in arg:
        if i.islower():
            return True
            break
        else:
            continue
    return False

def digit_check(arg):
    for i in arg:
        if i.isdigit():
            return True
        else:
            continue
    return False
    
def special_check(arg):
    for i in arg:
        if i in ["*","!","@","#","^","&","_","–","=","[","]","|",";","~",",",".","/","?"]:
            return True
        else:
            continue
    return False

def allowed_check(arg):
    for i in arg:
        if i.isalnum():
            continue
        elif special_check(i) is True:
            continue
        else:
            return False
    return True

def element_check(arg):
    if arg >= 3:
        return True
    else:
        return False

def password_check():
    while True:
        valid_password = False
        placeholder = False
        successful_element = 0
        # calling password_input function
        user_password = passwordchecker.password_input()
        # checking for unsupported characters
        if allowed_check(user_password) == False:
            print("INVALID PASSWORD", "Password contains an unsupported character.", sep = "\n")
            continue

        # checking for 3 or more elements
        # uppercase check
        for x in range(0, len(user_password)):
            placeholder = passwordchecker.uppercase_check(user_password[x])
            # uppercase_check leaves placeholder as "True"
            if placeholder:
                break
            else:
                continue

        valid_password = placeholder

        if valid_password:
            successful_element += 1
        # lowercase check
        valid_password = lowercase_check(user_password)
        if valid_password:
            successful_element += 1
        # digit check
        valid_password = digit_check(user_password)
        if valid_password:
            successful_element += 1
        # special check
        valid_password = special_check(user_password)
        if valid_password:
            successful_element += 1
        # element check
        valid_password = element_check(successful_element)
        # print statements
        if valid_password:
            print("VALID PASSWORD.")
            break
        else:
            print("INVALID PASSWORD", "Password does not contain 3 or more required elements.", sep="\n")
            
password_check()

        
    
    
