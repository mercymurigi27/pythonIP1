#!/usr/bin/env python3.8

from User import find_by_user_name, user_acc
from credentials import credential
import random
import string




def create_newUser(username,password,email):
    """
    creates new user account
    """
    new_User = user_acc(username,password,email)
    print("User created")
    return new_User

def save_newUser(User):
    """
    saves new user log in details

    """
    User.save_newUser()  



def del_newUser(User):
    """
    deletes any unwanted user log in detail from user account list
    """ 
    User.delete_User()
    print("Succefully deleted")


def find_User(user_name):
    """
   finds login details by username
    """  
    return user_acc.find_by_user_name(user_name)

def display_users():
    """
    return all users saved
    """  
    return user_acc.display_users() 


def create_new_cred(cred_username, cred_passward):
   '''
    creates new instances of user's credentials
   '''
   new_cred = credential(cred_username, cred_passward)
   return new_cred 

def save_credential(credentials):
  '''
  function to save the newly credential detail created
  '''
  credentials.save_credential()   

def delete_credential(credentials):
  '''
  deletes of unwanted user credentials
  '''
  credentials.del_credential()  
  print("Succefully deleted") 




def main():
    print("Hello, wonderful to have you here. kindly input your name to continue")
    user_name = input()
    print (f'Hi {user_name}. How can we help today?')

    print ('\n')
    

    while True:
        print('Lets help you navigate use:LC-log in to account, NC-creates new account, VC-displays lists of acc and passwards, DC- deletes accounts you dont want to keep,E-exits application')
        short_code = input().lower()


        if short_code == 'NC':
            print('lets create a new contact')
            print('-'*10)

            print('user_name')
            username = input()
            
            print('email')
            email = input()

            print('passward')
            passward = input()

            

            save_newUser(create_newUser(user_name,email, passward))

            print('\n')
            print (f'new user_acc {username} has been successfully created')
            print('\n')

        elif short_code == 'DC':
            if del_newUser(user_acc):
                print('Are you sure?....Y/N?')
                print('enter username')
                user_name = input()
                print('enter passward')
                passward = input()

                print ('\n')
                del_newUser(find_by_user_name(user_name))
                print ('{user_acc.user_name} has been successfully deleted')

        elif short_code == 'VC':
              if display_users():
                  print('here are all the accounts you have saved\n')
                  for user in display_users():
                      print(f'{user_acc.username}{email} {credential.acc_name} {user_acc.passward}')

        elif short_code == 'E':
            print('Have a beautiful day')   
            break
        else:
            print('something went wrong, command not found. check your commans and start again. Thank you')



if __name__ == '__main__':
    main()