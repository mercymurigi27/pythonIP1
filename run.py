#!/usr/bin/env python3.8
from User import user_acc
from credentials import credential
import random
import string




def create_newUser(username,password,email):
    """
    creates new user account
    """
    new_User = user_acc(username,password,email)
    return new_User

def save_newUser(User):
    """
    saves new user log in details

    """
    User.save_User()  

def del_newUser(User):
    """
    deletes any unwanted user log in detail from user account list
    """ 
    User.delete_User()


def find_User(user_name):
    """
   finds login details by username
    """  
    return user_acc.find_by_user_name(user_name)

    
