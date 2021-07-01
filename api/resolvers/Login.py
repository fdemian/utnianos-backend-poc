import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import User #, UserActivation
from api.utils.utils import (delay_time, parse_config_file)
from api.utils.crypto import check_password, hash_password
from api.utils.auth import get_user_token
from os import path

def get_context(config_path):
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    settings = parse_config_file(config_file_path)
    db_session = get_session(config_file_path)

    return {
      'settings': settings,
      'db_session': db_session
    }

class Login(graphene.Mutation):
    class Arguments:
      username = graphene.String()
      password = graphene.String()

    ok = graphene.Boolean()
    id = graphene.Int()
    avatar = graphene.String()
    username = graphene.String()
    fullname = graphene.String()
    email = graphene.String()
    link = graphene.String()

    def mutate(root, info, username, password):

        #print(info.context)

        config_file = '../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        context = get_context(config_file_path)

        ok = True
        user = try_login_user(username, password, context)

        if user is None:
           raise Exception('404', 'User not found.')

        return Login(
          ok=ok,
          id=int(user['user']['id']),
          avatar=user['user']['avatar'],
          username=user['user']['username'],
          fullname=user['user']['fullname'],
          email=user['user']['email'],
          link=user['user']['link']
        )


def try_login_user(username, password, context):
    user = authenticate_user(username, password, context)
    expiration_time = context['settings']['jwt']["expiration"]

    if user is not None:
        jwt_token = get_user_token(user, context, expiration_time)

        response = {
          'token': jwt_token,
          'user': user
        }

        return response

    return None



# UTILITY FUNCTIONS.
def get_mock_user():
    mock_user = User()
    mock_user.username = "fakeuser"
    mock_user.password = "fake_password"
    mock_user.lockout_time = datetime.now()
    mock_user.failed_attempts = 0
    mock_user.email = "fake@fake.com"
    mock_user.fullname = "Fake Mega User"
    mock_user.valid = False

    return mock_user


def user_to_dict(user):

    user_link = '/users/' + str(user.id) + "/" + user.username

    payload = {
      'id': user.id,
      'avatar': user.avatar,
      'username': user.username,
      'fullname': user.fullname,
      'email': user.email,
      'link': user_link
    }

    return payload


def get_user_if_exists(session, username):
    try:
       user = session.query(User).filter(User.username == username).one()
       return user

    except MultipleResultsFound:
       return None

    except NoResultFound:
       return None


def user_is_locked(session, user, lockout_time):

     if user.lockout_time is None:
         return False

     time_elapsed = datetime.now() - user.lockout_time

     if time_elapsed.seconds > (lockout_time*60):
         user.lockout_time = None
         session.merge(user)
         session.commit()
         return False
     else:
         return True


def unlock_user(session, user):
    user.failed_attempts=0
    user.lockout_time=None
    session.merge(user)
    session.commit()


def register_failed_login(session, user, max_login_tries):
    user.failed_attempts = user.failed_attempts + 1

    # If the user reached the maximum number of tries.
    if user.failed_attempts is max_login_tries:
       user.lockout_time = datetime.now()

    session.merge(user)
    session.commit()

    return user


def authenticate_user(username, password, context):

    settings = context['settings']
    db_session = context['db_session']
    password_is_correct = False
    user = get_user_if_exists(db_session, username)
    max_login_tries = settings["account"]["maxLoginTries"]
    login_delay = settings["account"]['loginDelayTimeStep']
    lockout_time = settings["account"]['lockoutTimeWindow']

    if user is None:
        #logger.info("Requested unexistent user: " + username)
        user = get_mock_user()
        hash_password(user.password, '')
        user_exists = False
    else:
        #logger.info("User exists and is: " + username)
        #logger.info(user.failed_attempts)
        user_exists = True
        #delay_time(login_delay, user.failed_attempts)  # Wait an ammount of time proportional to the number of failed attempts.
        check_pass = check_password(password, user.password, user.salt)

        # User tried to login the maximum number of allowed tries.
        if user_is_locked(db_session, user, lockout_time):
          print(user_is_locked)
          #logger.info("User is locked: " + username)
          return None

        """
         If the user is valid and it exists verify that the password was input correctly.
         If not, register the failed attempt in the database.
        """
        if user.valid and user_exists:
            #logger.info("User is valid and exists: ")
            if check_pass:
                password_is_correct = True
            else:
                #logger.info("User is invalid or does not exist. ")
                password_is_correct = False
                #register_failed_login(db_session, user, max_login_tries)
        else:
            password_is_correct = False

        if password_is_correct:
            #logger.info("Password is correct. ")
            user_dict = user_to_dict(user)
            return user_dict
        else:
            return None
