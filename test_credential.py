import unittest

from credentials import credential


class Testcredential(unittest.TestCase):
  '''
  TestCredentials test class that defines test cases for Credentials class behavior
  '''

  def setUp(self):
      '''
      set up method defines actions to be run before any test cases
      '''
      self.new_user_credential = credential("mercymurigi", "murigi123")

  def tearDown(self):
      '''
       method that performs clean up after each test case has run
      '''
      credential.credentials_list = []

  def test_init(self):
       '''
        test_init test case that checks if credential instance were initialized correctly
       '''

       self.assertEqual(self.new_user_credentials.user_name, "mercymurigi")
       self.assertEqual(self.new_user_credential.passward, "mercy1234")


  def test_save_credentials(self):
      '''
         est_save_credentials test case to check if credentials are added to the user_cred_list
      '''

      self.new_user_credential.save_credential()
      self.assertEqual(len(credential.credentials_list), 1)   

  def test_save_multiple_contacts(self):
      '''
       test_save_multiple_contacts test case to check if we can store multiple oblects in our credentials list
      '''
      self.new_user_credential.save_credential()

      test_credential = credential("raymarlvis", "ray@123")
      test_credential.save_credential()

      self.assertEqual(len(credential.credentials_list), 2)

  def test_delete_credential(self):
      '''
       test_delete_credential test case to remove saved credential from user_cred_list
      '''
      self.new_user_credential.save_credential()
      test_credential = credential("raymarlvis", "ray@123")
      test_credential.save_credential()

      self.new_user_credential.delete_credential()
      self.assertEqual(len(credential.credentials_list), 1)
   

  def test_search_by_name(self):
       '''
        test case that checks if a stored credential can be found when searched by name
       '''
       self.new_user_credential.save_credential()
       test_credential = credential("raymarlvis", "ray@123")
       test_credential.save_credential()

       searched_cred = credential.search_by_name("mercymurigi")
       self.assertEqual(searched_cred, self.new_user_credential)



  def test_display_all_cred(self):
       '''
         test that returns a list of all saved credentials
      '''
       self.assertEqual(credential.display_credentials(), credential.credentials_list)


if __name__ == '__main__':
  unittest.main()    