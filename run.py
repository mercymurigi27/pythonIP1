#!/usr/bin/env python3.8

from User import find_by_user_name, save_user_acc, user_acc
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

def display_credentials():
  '''
  function that rerturns all saved credentials
  '''
  return credential.display_cred()

def generate_random_passward():
  '''
  function that generates random user passcode digits
  '''
  string_code = string.ascii_letters + string.digits + string.punctuation

  while True:
    try:
      code_length = int(input('Enter password length\n'))
      if code_length <4:
        print("-"*10)
        print("Length must be atleast 4 digits")
        print("-"*10)
        continue

      rand_code = random.sample(string_code, code_length)

    except ValueError:
      print("-"*10)
      print("Error::Please input a valid number")
      print("-"*10)
      continue

    else:
      gen_password = ''.join(rand_code)
      return gen_password


def main():
    print("Hello, wonderful to have you here. kindly input your name to continue")
    user_name = input()
    print (f'Hi {user_name}. How can we help today?')

    print ('\n')
    

    while True:
        print('choose an action')
        print(' log in select LG, IF YOU HAVE AN EXISTING ACCOUNT')
        print('IF YOU DONT HAVE AN ACCOUNT,select NC to create an account')


        short_code = input().upper()

        if short_code == "LI":
            print("\n")
            print("LOGIN INTO YOUR ACCOUNT")
            print("_"*25)
        user_name = input("Enter your Username: ")
        passward = input("Enter your Password: ")
        print(' WELCOME')



        if short_code == 'NC':
            print('\n')
            print('lets create a new account')
            print('-'*20)
            
            print('acc_name')
            acc_name = input('enter your account name')
            while acc_name =="":
              print("-"*10)
              print("Incorrect input!!!")
              print("-"*10)
            acc_name = input('enter account name')  

            print('user_name')
            user_name = input("enter user name")
            while user_name == "":
             print("-"*10)
             print("Incorrect input!!!")
             print("-"*10)
            user_name = input("Enter username: ")
            
            print('email')
            email = input()

            print('passward')
            passward = input("Enter password: ")
            while len(passward)<4:
             print("Passward is too short. Must be atleast 4 characters.")
             print("-"*10)
            passward = input("Enter password: ")

            verify_passward = input('verify passward:')
            
            while passward != verify_passward:
              print("-"*15)
              print("Error:: Passwords did not match. Retry!")
              print("-"*15)
              passward = input("Enter password: ")
            while len(passward)<4:
               print("Password too short. Must be atleast 4 characters.")
               print("-"*10)
               passward = input("Enter password: ")

            verify_passward = input("verify password: ")

            
            print("\n")
            print(f"-----CONGRATULATIONS {user_name.upper()}!!! YOUR ACCOUNT HAS BEEN CREATED SUCCESSFULLY-----")
            print("\n")
            print("-->Kindly proceed to LOGIN")
            print("\n")
            print("LOGIN INTO YOUR ACCOUNT")
            print("_"*25)
            keyedin_user_name = input("Enter your Username: ")
            keyedin_passward = input("Enter your Password: ")

        #check if correct username and password have been entered
        while user_name != user_name or passward != passward:
           print("-"*15)
           print("Invalid username or password")
           print("-"*15)
           user_name = input("Enter your Username: ")
           passward = input("Enter your Password: ")

        else:
           print("\n")
           print(f"Logged In as {user_name.capitalize()}")
           print("_"*30)
           print(f"Hello {user_name.capitalize()}. Welcome to your new  Account")
           print("-"*25)
           print("Keep all your account passwords safe and secure in one place")
    

        while True:
          print('\n')
          print('choose an option')
          print('CN...for new credentials, DL..to delete credentials, SC..to search for existing credential,DP...to display all saved credentioals')
          short_code= input().upper()

          if short_code== "CN":
            print("\n")
            print("CREATE AND SAVE CREDENTIAL")
            print("_"*25)
            credential_username = input("Enter Account Name: ")
          while True:
              print("\n")
              print("Select option for password generation")
              print("-"*10)
              print("\IN--> to input the password yourself")
              print("\GT--> to auto-generate password")
              print("\ex--> to leave prompt")

              p_code = input("Answer: ").upper()

              if p_code == "IN":
                print("\n")
                cred_password = input("Enter Account Password: ")
                print("-"*20)
                while len(cred_password)<4:
                  print("----> Password too short. Must be atleast 4 characters.")
                  print("-"*10)
                  cred_password = input("Enter Account Password: ")
                break

              elif p_code == "GT":
                cred_password = generate_random_passward()
                print("-"*20)
                print("Password successfully generated")
                print("-"*20)
                break
              elif p_code == 'ex':
                break
              else:
                print("Incorrect option. Try again!")
              created_credential = create_new_cred(credential_username, cred_password)
              save_credential(created_credential)  
              print('\n')
              print('welcome, your account has been created and saved successfully.')

              short_code == input().upper() 

          if short_code == "DL":
               
            print("\n")
            print("DELETE CREDENTIAL")
            print("_"*20)
            cred_to_delete = input("Enter Account Name of the credential you want to delete: ")
          cred_found = search_cred(cred_to_delete)
          delete_credential(cred_found)
          print("Credential successfully deleted!")

          if short_code == "DP":
           if display_credentials() == None:
              print("No credentials found to display yet")

          else:
              print("\n")
              print("AVAILABLE CREDENTIALS")
              print("_"*20)
              print("\tAccount Name ---|--- \tPassword")
              for credential in display_credentials():
                print(f"\t-->{credential.credential_username} ---|--- {credential.credential_passward}")

          if short_code == "SC":
            print("\n")
            print("SEARCH AVAILABLE CREDENTIALS")
            print("_"*20)
            cred_to_search = input("Enter name to search: ")
            if search_cred(cred_to_search):
              found_cred = search_cred(cred_to_search)
              print(f"Password for Account {cred_to_search}: {found_cred.cred_passward}")
            else:
              print("-"*20)
              print("That Credential was not found!")
              print("-"*20)

              if short_code == "ex":
               print("\n")
               print("Are you sure you want to exit this application?\nY/N")
            response = input("Answer: ").upper()
            if response == "Y":
              print("-"*20)
              print("\tThank you for using this application. \nSee you again next time!")
          
        else:
          print('something went wrong, command not found. check your commans and start again. Thank you')


        # elif short_code == 'DC':
        #     if del_newUser(user_acc):
        #         print('Are you sure?....Y/N?')
        #         print('enter username')
        #         user_name = input()
        #         print('enter passward')
        #         passward = input()

        #         print ('\n')
        #         del_newUser(find_by_user_name(user_name))
        #         print ('{user_acc.user_name} has been successfully deleted')

        # elif short_code == 'VC':
        #       if display_users():
        #           print('here are all the accounts you have saved\n')
        #           for user in display_users():
        #               print(f'{user_acc.username}{email} {credential.acc_name} {user_acc.passward}')

        # elif short_code == 'E':
        #     print('Have a beautiful day')   
        #     break
        # 



if __name__ == '__main__':
    main()