

class credential:

    """
    class that generates accounts credentials and passward to save.
    """

    credentials_list = []

    def __init__(self,cred_username,cred_passward):

        """
        it defines the objects of our class

        args:
        args:
        cred_username : new_credentials_user_name.
        cred_passward : new_credentials_cred_passward.

        """   
        self.cred_username = cred_username
        self.cred_passward = cred_passward

    def save_credential(self):
        """
        this saves the credential details into the credential list variable
        """
        credential.credentials_list.append(self)

    def delete_credential(self):
        """
        deletes users log in credentials from credential list variable
        """    
        credential.credentials_list.remove(self)


    @classmethod
    def search_by_name(cls, cred_username):   
        """
        a method that helps the user search through credential class via cred_username and returns if there is a match
        """
        for credential in cls.credentials_list:
            if credential.cred_username == cred_username:
                return credential

    @classmethod
    def display_credentials(cls):    
        """
        displays a list of all accounts saved in credential class
        """

        return cls.credentials_list