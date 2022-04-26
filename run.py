#!/usr/bin/env python3.8


from User import  user_acc
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
    credentials.delete_credential()  
    print("Succefully deleted") 

def display_credential():
    '''
    function that rerturns all saved credentials
    '''
    return credential.display_credentials()
  

def search_cred(user_name):
    return credential.search_by_name(user_name)


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

    while True:
        print('choose an action')
        print(' log in select LG, IF YOU HAVE AN EXISTING ACCOUNT')
        print('IF YOU DONT HAVE AN ACCOUNT,select NC to create an account')


        short_code = input().upper()

        if short_code == "LG":
            print("\n")
            print("LOGIN INTO YOUR ACCOUNT")
            print("_"*25)
            user_name = input("Enter your Username: ")
            passward = input("Enter your Password: ")
            print(' WELCOME')



        elif short_code == 'NC':
            print('\n')
            print('lets create a new account')
            print('-'*20)
            
            print('acc_name')
            acc_name = input('enter your account name:  ')
            while acc_name =="":
              # print("-"*10)
              print("Incorrect input!!!")
              print("-"*10)
              acc_name = input('enter account name:  ')  
  
              print('user_name')
              user_name = input("enter user name:  ")
              while user_name == "":
                print("-"*10)
                print("Incorrect input!!!")

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
                    # print("-"*2)
                    print("Error:: Passwords did not match. Retry!")
                    # print("-"*15)
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
        user_name = input("Enter your Username: ")
        passward = input("Enter your Password: ")

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
            cred_username= input("Enter user Name: ")
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

            created_credential = create_new_cred(cred_username, cred_password)
            save_credential(created_credential)  
            print('\n')
            print('welcome, your account has been created and saved successfully.')

          # short_code == input().upper() 

          elif short_code == "DL":
                
              print("\n")
              print("DELETE CREDENTIAL")
              print("_"*20)
              cred_to_delete = input("Enter Account Name of the credential you want to delete: ")
              cred_found = search_cred(cred_to_delete)
              delete_credential(cred_found)
              print("Credential successfully deleted!")

          elif short_code == "DP":
              if display_credential() == None:
                  print("No credentials found to display yet")

              else:
                  print("\n")
                  print("AVAILABLE CREDENTIALS")
                  print("_"*20)
                  print("\tAccount Name ---|--- \tPassword")
                  for credential in display_credential():
                    print(f"\t-->{cred_username} ---|--- {cred_password}")

          elif short_code == "SC":
              print("\n")
              print("SEARCH AVAILABLE CREDENTIALS")
              print("_"*20)
              cred_to_search = input("Enter name to search: ")
              if search_cred(cred_to_search):
                cred_search = search_cred(cred_to_search)
                print(f"account name is {cred_search.cred_username} and the password is {cred_search.cred_passward} ")
              else:
                print("-"*20)
                print("That Credential was not found!")
                print("-"*20)

          elif short_code == "ex":
                print("\n")
                print("Are you sure you want to exit this application?\nY/N")
                response = input("Answer: ").upper()
                if response == "Y":
                    print("-"*20)
                    print("\tThank you for using this application. \nSee you again next time!")
          
          else:
            print('something went wrong, command not found. check your commans and start again. Thank you')


      


if __name__ == '__main__':
    main()