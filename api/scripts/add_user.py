from getpass import getpass
from api.models.sessionHelper import get_session
from api.models.models import User
from api.utils.crypto import hash_password
from os import path, urandom

"""
Actually save the user.
"""
def do_save_user(user_to_save, session, *args, **kwargs):
    # TODO: document this.

    is_valid = kwargs.get('is_valid', None)

    salt = urandom(16) # Generate 16 random bits.
    hashed_pass = hash_password(user_to_save["password"], salt)

    user = User()
    user.username = user_to_save["username"]
    user.password = hashed_pass
    user.salt = salt
    user.fullname = user_to_save["name"]
    user.email = user_to_save['email']
    user.failed_attempts = user_to_save['failed_attempts']

    if is_valid is None:
        user.valid = False
    else:
        if is_valid is True:
           user.valid = True

    user.valid = is_valid  # A user is not valid until his/her email has ben verified.
    user.avatar = None
    session.add(user)
    session.commit()

    return user

config_file = '../../config.json'
config_file_path = path.join(path.dirname(__file__), config_file)

def add_user():

    username = input("Choose a username: ")
    password = getpass("Choose a password: ")
    email = input("Enter a valid email address: ")
    name = input("Choose a user name: ")
    print(password)

    user = {
      'username': username,
      'password': password,
      'email': email,
      'name': name,
      'avatar': None,
      'failed_attempts': 0,
      'lockout_time': None,
      'type': 'database'
    }

    session_object = get_session(config_file_path)
    session = session_object()
    do_save_user(user, session, is_valid=True)
