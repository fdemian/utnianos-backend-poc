import graphene
from api.models.models import Course, db_session
from os import path

class CourseObj(graphene.ObjectType):
      code = graphene.String()
      name = graphene.String()
      year = graphene.Int()

def resolve_course_objects(self, context):
    all_types = db_session.query(Course).all()
    return all_types
