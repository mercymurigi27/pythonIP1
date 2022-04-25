import unittest
from User import user_acc

class Testuser_acc(unittest.TestCase):

    """
    test class for user acc behaviour
    """
def setUp(self):

    self.new_User = user_acc("mercymurigi","mercy1234","murigi@yahoo.com")    

def test_init(self):

    self.assertEqual(self.new_User.user_name,"mercymurigi")
    self.assertEqual(self.new_User.passward,"mercy123")
    self.assertEqual(self.new_User.email,"murigi@yahoo.com")



if __name__ == '__main__':
    unittest.main()    