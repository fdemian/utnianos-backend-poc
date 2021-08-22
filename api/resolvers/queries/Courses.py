import graphene
from api.models.sessionHelper import get_session
from api.models.models import Course #, UserActivation
from os import path

class CourseObj(graphene.ObjectType):
      code = graphene.String()
      name = graphene.String()
      year = graphene.Int()

def resolve_course_objects(self, context):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    all_types = db_session.query(Course).all()

    return all_types
