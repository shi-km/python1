# Passwordlocker

## Built By [George kamau](https://github.com/shi-km/)

## Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

## User Stories
These are the behaviours/features that the application implements for use by a user.

As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./run.py** | Do you want to sign up or login : Click 's' to sign up or 'l' to login |
| Display prompt for creating an account | **Enter: s** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: l** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Use these short codes : sc - save an already existing account credential, cc - create a new credential, vc - view your credentials, fc -find a credential, lo -logout |
| Display prompt for saving an already existing credential | **Enter: sc** | Enter the site name, your username and password |
| Display a list of credentials | **Enter: vc** | Prints a list of saved credentials |
| Exit application | **Enter: lo** | logout the current logged in account |

## SetUp / Installation Requirements
### Prerequisites
* python 3.6
* pip

### Cloning
* In your terminal:
        
        $ git clone https://github.com/shi-km/python1/
        $ cd Password_locker

## Running the Application
* To run the application, in your terminal:

        $ chmod +x password_locker.py
        $ ./run.py
        
## Testing the Application
* To run the tests for the class file:

        $ python3.6 test_locker.py
        
## Technologies Used
* Python3.6

## License
MIT &copy;2019 [George kamau](https://github.com/shi-km/)

