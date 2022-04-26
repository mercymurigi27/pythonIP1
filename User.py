import re


class user_acc:
    
    """
    class that generates user log in account
    """

    User_accounts_list = [] #empty user accounts details

    def __init__(self,acc_name, user_name, passward, email):
        """
        deifne properties for our object
        
        Args:
            acc_name:new user_acc name.
            user_name: new user_acc name.
            passward:passward.
            email: new user_acc email address. 
        """ 
        self.acc_name = acc_name
        self.user_name = user_name
        self.passward = passward
        self.email = email

    def save_user_acc(self):
        """
        saves new user detail and appends them to the user accounts list
        """
        user_acc.User_accounts_list.append(self)

    def delete_user_acc(self):
        """
        delete saved user account from user account details
        """
        user_acc.User_accounts_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        """"
        finds a user by name username and returns if its a match
        """    
        for User in cls.User_accounts_list:
            if User.user_name == user_name:
                return User

    @classmethod
    def display_users(cls):
        """
        a method that displays a list of all saved users
        """
        return cls.User_accounts_list
    
             