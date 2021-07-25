import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import User #, UserActivation
from api.utils.utils import (delay_time, parse_config_file)
from api.utils.crypto import check_password, hash_password
from api.utils.auth import get_user_token
from datetime import datetime
from .CareerPlan import CareerPlanObj
from os import path
from flask_graphql_auth import query_header_jwt_required

class UserObject(graphene.ObjectType):

      id = graphene.Int()
      avatar = graphene.String()
      username = graphene.String()
      fullname = graphene.String()
      email = graphene.String()
      link = graphene.String()
      careerPlan = graphene.Field(CareerPlanObj)

def resolve_user_id(self, info, id):
        config_file = '../../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        db_session = get_session(config_file_path)
        user = get_user_if_exists(db_session, id)

        if not user:
            raise Exception('Requested user does not exist.')
        else:
            return user_to_dict(user)

def get_user_if_exists(session, id):
    try:
       user = session.query(User).filter(User.id == id).one()
       return user

    except MultipleResultsFound:
       return None

    except NoResultFound:
       return None


def user_to_dict(user):

    user_link = '/users/' + str(user.id) + "/" + user.username

    payload = {
      'id': user.id,
      'avatar': user.avatar,
      'username': user.username,
      'fullname': user.fullname,
      'email': user.email,
      'link': user_link,
      'careerPlan': user.career_plan
    }

    return payload
