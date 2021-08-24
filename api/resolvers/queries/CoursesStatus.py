import graphene
from api.models.sessionHelper import get_session
from api.models.models import CoursesStatus
from os import path

class CoursesStatusObj(graphene.ObjectType):
    id = graphene.Int()
    user_id = graphene.Int()
    course_code = graphene.String()
    completion_code = graphene.String()

def _resolve_courses_status_id(self, context, id):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)

    statuses = db_session.query(CoursesStatus).filter(
        CoursesStatus.user_id == id
    ).all()

    return statuses
