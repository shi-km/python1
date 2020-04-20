#!/usr/bin/env python3.6
from locker import *
import secrets
import string

def create_account(user_name, password):
    '''
    Function to create a new user account
    '''

    new_user = User(user_name, password)
    return new_user

def save_account(user):
    '''
    Function to save user account
    '''
    User.create_account(user)

def login(user_name, password):
    '''
    Function that check if a user exists with that number and return a Boolean
    '''
    return User.user_exist(user_name, password)

def create_credential(account_name, user_name, password):

    '''
    Function to create a new credential
    '''
    new_credential = Credential(account_name, user_name, password)
    return new_credential

def save_credential(credential):
    '''
    Function to save a credentials
    '''
    return Credential.save_credential(credential)

def find_credential(account_name):
    return Credential.find_by_account_name(account_name)

def view_credential():
    return Credential.view_all_credentials()

def delete_credential():
    return Credential.delete_credential()

def generate_password(pass_len):
    '''
    generate a new password
    Args:
    pass_len: preffered password length.
    '''

    return "".join(secrets.choice(string.ascii_letters+string.digits) for i in range(pass_len))


def main():
    print("Hello! Welcome to One Pass")
    logged_in = False 

    while True:
        print("Do you want to sign up or login")
        print("Click 's' to sign up or 'l' to login")
        answer = input()
        if answer == "l":
            print("Enter your username: ")
            user_name = input()
            print("Enter your password: ")
            password = input()

            logged_in = login(user_name, password) if answer == 'l' else False

            while logged_in:
                print("Use these short codes : sc - save an already existing account credential, cc - create a new credential, vc - view your credentials, fc -find a credential, lo -logout ")
                code = input()

                if code == "sc":
                    print("Create new credential")

                    print("Enter the name of the account credential")
                    account_name = input()

                    print("Enter the account credential username")
                    user_name = input()

                    print("Enter the password of the account")
                    password = input()

                    save_credential(create_credential(account_name, user_name, password))

                    print(f"Account credentials for {account_name} has been saved")
                    print("\n")

                elif code == "cc":
                    print("Enter the name of the account credential")
                    account_name = input()

                    print("Enter the account credential username")
                    user_name = input()


                    print("Password:")
                    print("Would you like to automatically generate your password? y/n")
                    passs = input()

                    if passs == "y":
                        print("Enter your preffered password length")
                        pass_len = int(input())
                        password = generate_password(pass_len)
                        print(f"Your new password for {account_name} is {password}")

                    elif passs == "n":
                        print("Create your own password:")
                        password = input()

                    else:
                        print("Invalid choice!")

                    save_credential(create_credential(account_name, user_name, password))

                    print(f"Account credentials for {account_name} has been saved")
                    print("\n")

                elif code == "vc":
                    if view_credential():
                        print("Here is a list of all your credentials")
                        print('\n')

                        for credential in view_credential():
                            print(f"Account Name ..... {credential.account_name}")
                            print(f"User Name ..... {credential.user_name}")
                            print(f"Password   .....   {credential.password}")
                            print('\n')
                    else:
                                    print('\n')
                                    print("You dont seem to have any credentials saved yet")
                                    print('\n')
                
                elif code == "fc":
                    print("Enter the account credential name you want to search for")

                    name= input()
                    found_credential = find_credential(name)
                    if found_credential:
                        print(f"Your username for your {found_credential.account_name} account is {found_credential.user_name} and it's password is {found_credential.password}")
                        print("\n")
                
                
                    else:
                            print("That credential does not exist")

                elif code == "lo":
                    print("logging out...")
                    exit()

                else:
                    print("Invalid code!")

            else:
                print("Wrong username or password.Try again")
                print("\n")
                # quit()


        elif answer == "s":
            print("Create new account")

            print("Username:")
            user_name = input()

            if user_name:
                print("password:")
                password = input()
        
                save_account(create_account(user_name, password))
                print(f"Account for {user_name} has been created")
                print("\n")
            else:
                print("Invalid Username")

        else:
            print("Invalid choice!!")

if __name__ == "__main__":
    main()