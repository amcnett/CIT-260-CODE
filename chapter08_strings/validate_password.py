# This program gets information and reports login name to the user.
# It also takes the password from the user and validates it.

import login # reminder of how to use modules!

def main():
    # Get login name
    first = input('Enter your first name: ')
    last = input('Enter your last name: ')
    idnumber = input('Enter your student ID number: ')
    print(login.get_login_name(first, last, idnumber))

    # Get a password from the user.
    password = input('Enter your password: ')

    # Validate the password.
    while not login.valid_password(password):
        print('That password is not valid.')
        password = input('Enter your password: ')

    print('That is a valid password.')

# Call the main function.
if __name__ == '__main__':
    main()
