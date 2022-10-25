"""
Name: Hana Pak
Assignment: 6
Problem: 3
Partner: Partner out of range
"""

# import statement
import passwordchecker

# defining functions
def lowercase_check(arg):
    for i in arg:
        if i.islower():
            return True
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
        if i in ["*", "!", "@", "#", "^", "&", "_", "–", "=", "[", "]", "|", ";", "~", ",", ".", "/", "?"]:
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


def password_checker():
    # Get a user's password
    is_password_valid = False
    temp = False  # used for wrong function wrapper
    successful_checks = 0
    user_password = passwordchecker.password_input()

    # Allowed check, exit condition
    if allowed_check(user_password) == False:
        print("INVALID PASSWORD.  PASSWORD CONTAINS AN UNSUPPORTED CHARACTER.")
        return

    # Uppercase check
    for index in range(0, len(user_password)):
        temp = passwordchecker.uppercase_check(user_password[index])
        if temp:
            break
        else:
            continue

    is_password_valid = temp
    if is_password_valid:
        successful_checks += 1

    # Lowercase check
    is_password_valid = lowercase_check(user_password)
    if is_password_valid:
        successful_checks += 1

    # Digit check
    is_password_valid = digit_check(user_password)
    if is_password_valid:
        successful_checks += 1

    # Special check
    is_password_valid = special_check(user_password)
    if is_password_valid:
        successful_checks += 1

    # Element check
    is_password_valid = element_check(successful_checks)

    # Print stuff
    if is_password_valid:
        print("VALID PASSWORD.")
    else:
        print("INVALID PASSWORD.  PASSWORD DOESN'T HAVE REQUISITE ELEMENTS.")


password_checker()