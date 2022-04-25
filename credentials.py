class credentials:

    """
    class that generates accounts credentials and passward to save.
    """

    credentials_list = []

def __init__(self,acc_name,passward):

    """
    it defines the objects of our class

    args:
    args:
    acc_name : new_credentials_acc_name.
    passward : new_credentials_passward.

    """   
    self.acc_name = acc_name
    self.passward = passward

def save_credentials(self):
    """
    this saves the credential details into the credential list variable
    """
    credentials.credentials_list.append(self)

def delete_credentials(self):
    """
    deletes users log in credentials from credential list variable
    """    
    credentials.credentials_list.remove(self)


@classmethod
def find_by_accountname(cls,acc_name):   
   """
   a method that helps the user search through credential class via acc_name and returns if there is a match
   """
   for credentials in cls.credentials_list:
       if credentials.acc_name == acc_name:
           return acc_name

