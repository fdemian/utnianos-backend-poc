import graphene
from api.models.sessionHelper import get_session
from api.models.models import ContribType #, UserActivation
from os import path

class ContribTypeObj(graphene.ObjectType):
      id = graphene.Int()
      name = graphene.String()

def resolve_contrib_objects(self, context):
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    all_types = db_session.query(ContribType).all()

    return all_types
