import graphene
from api.models.sessionHelper import get_session
from api.models.models import CoursePrerrequisites #, UserActivation
from os import path

class CoursePrerrequisitesObj(graphene.ObjectType):
    id = graphene.Int()
    course_id = graphene.Int()
    prerrequisite_id = graphene.Int()
    type = graphene.String()
    completion_id = graphene.Int()


def resolve_prerreq_objects(self, context):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    prerrequisites = db_session.query(CoursePrerrequisites).all()

    return prerrequisites
