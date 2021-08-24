import graphene
from api.models.models import CoursesStatus, db_session
from os import path

class CoursesStatusObj(graphene.ObjectType):
    id = graphene.Int()
    user_id = graphene.Int()
    course_code = graphene.String()
    completion_code = graphene.String()

def _resolve_courses_status_id(self, context, id):
    statuses = db_session.query(CoursesStatus).filter(
        CoursesStatus.user_id == id
    ).all()

    return statuses
