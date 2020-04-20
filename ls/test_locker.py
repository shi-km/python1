import unittest
from locker import *


class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_user = User("George", "lim66")

    def tearDown(self):
        User.users_list = []

    def test_init(self):
        self.assertEqual(self.new_user.user_name, "George")
        self.assertEqual(self.new_user.password, "lim66")

    def test_create_account(self):
        self.new_user.create_account()

        self.assertEqual(len(User.users_list), 1)

    def test_save_multiple_accounts(self):
        self.new_user.create_account()

        new1_user = User("jim", "7Hh")
        new1_user.create_account()

        self.assertEqual(len(User.users_list), 2)

    def test_account_exists(self):
        self.new_user.create_account()

        new2_user = User("george", "hey44")
        new2_user.create_account()

        user_exists = User.user_exist("george", "hey44")

        self.assertTrue(user_exists)


class TestCredential(unittest.TestCase):
    '''
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    def setUp(self):
        self.new_credential = Credential("twitter", "kamau", "lim33")

    def tearDown(self):
        Credential.credentials_list = []

    def test_init(self):
        self.assertEqual(self.new_credential.account_name, "twitter")
        self.assertEqual(self.new_credential.user_name, "kamau")
        self.assertEqual(self.new_credential.password, "lim33")

    def test_save_credential(self):
        self.new_credential.save_credential()

        self.assertEqual(len(Credential.credentials_list), 1)

    def test_save_multiple_credentials(self):
        self.new_credential.save_credential()

        new1_credential = Credential("facebook", "george", "7fr")
        new1_credential.save_credential()

        self.assertEqual(len(Credential.credentials_list), 2)

    def test_find_by_account_name(self):
        self.new_credential.save_credential()

        new2_credential = Credential("instagram", "george", "harf")
        new2_credential.save_credential()

        found_credential = Credential.find_by_account_name("instagram")

        self.assertEqual(found_credential.password, new2_credential.password)

    def test_view_all_credentials(self):

        self.assertEqual(Credential.view_all_credentials(), Credential.credentials_list)

    def test_delete_credential(self):
        self.new_credential.save_credential()

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credentials_list), 0)


if __name__ == "__main__":
    unittest.main()