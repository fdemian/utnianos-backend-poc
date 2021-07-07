import graphene
from api.models.sessionHelper import get_session
from api.models.models import User
from api.scripts.add_user import do_save_user
from os import path

class CreateUser(graphene.Mutation):
    ok = graphene.String()
    id = graphene.Int()
    message = graphene.String()

    class Arguments:
        username = graphene.String()
        email = graphene.String()
        password = graphene.String()

    def mutate(self, info, username, email, password):
        config_file = '../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        db_session = get_session(config_file_path)

        #Check that the username does not already exist.
        user_exists = db_session.query(User).filter(User.username == username).first() is not None
        if user_exists:
           return CreateUser(
             ok=False,
             message="User already exists."
           )

        user = {
          'username': username,
          'password': password,
          'email': email,
          'name': "",
          'avatar': None,
          'failed_attempts': 0,
          'lockout_time': None,
          'type': 'database'
        }

        saved_user = do_save_user(user, db_session, is_valid=True)

        return CreateUser(
           ok=True,
           id=saved_user.id,
           message=""
        )
