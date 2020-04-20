class User:
    users_list = []

    def __init__(self, user_name, password):
        self.user_name = user_name
        self.password = password

    def create_account(self):
        User.users_list.append(self)

    @classmethod
    def user_exist(cls, user_name, password):
        '''
        Method that checks if a user exists from the users list.
        Args:
            user_name: user name to search if it exists
            password: password to search if it exists
        Returns :
            Boolean: True or false depending if the user exists
        '''
        for user in cls.users_list:
            if user.user_name == user_name and user.password == password:
                return True

        return False
class Credential:
    credentials_list = []

    def __init__(self, account_name, user_name, password):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_credential(self):
        Credential.credentials_list.append(self)

    @classmethod
    def find_by_account_name(cls, account_name):
        '''
        Method that takes in account name and returns a credential that matches that account name.

        Args:
            account_name: account name to search for
        Returns :
            credential that matches the account name.
        '''
        for credential in cls.credentials_list:
            if credential.account_name == account_name:
                return credential

    @classmethod
    def view_all_credentials(cls):
        '''
        method that returns the credential list
        '''
        return cls.credentials_list

    def delete_credential(self):
        Credential.credentials_list.remove(self)
    