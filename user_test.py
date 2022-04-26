import unittest
from User import user_acc


class Testuser_acc(unittest.TestCase):

    """
    test class for user acc behaviour
    """
def setUp(self):

    self.new_User = user_acc("mercymurigi","mercy1234","murigi@yahoo.com")    


def tearDown(self):
        '''
        tearDown method that cleans up after every test
        '''

        user_acc.User_accounts_list = []    

def test_init(self):

    self.assertEqual(self.new_User.user_name,"mercymurigi")
    self.assertEqual(self.new_User.passward,"mercy123")
    self.assertEqual(self.new_User.email,"murigi@yahoo.com")


def test_save_User(self):
        '''
        test_save_user tests case to find out if the user object is being saved
        '''

        self.new_User.save_user_acc()
        self.assertEqual(len(user_acc.User_accounts_list),1)


def test_delete_User(self):
        '''
         test if we can remove a user from out user accounts list
        '''


        self.new_User.save_User()
        test_user = user_acc('Test', 'user_name', 'mercy1234', 'test@user.com')
        test_user.save_user_acc()

        self.new_User.delete_User()

        self.assertEqual(len(user_acc.User_accounts_list),1)



def test_find_user_by_username(self):
        '''
        test to check if we can find a contact by username and display information
        '''

        self.new_User.save_user_acc()
        test_user = user_acc('Test','username', 'test@user.com','mercy1234')
        test_user.save_user_acc()

        found_user = user_acc.find_by_username('username')
        self.assertEqual(found_user.username, test_user.username)

def test_display_users(self):
     """
     test to see if the app is displaying the users saved
     """        
     self.assertEqual(user_acc.display_users(), user_acc.User_accounts_list)


if __name__ == '__main__':
    unittest.main()    