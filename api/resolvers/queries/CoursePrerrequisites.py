import graphene
from api.models.models import CoursePrerrequisites, db_session #, UserActivation
from os import path

class CoursePrerrequisitesObj(graphene.ObjectType):
    id = graphene.Int()
    course_code = graphene.String()
    prerrequisite_code = graphene.String()
    type = graphene.String()
    completion_code = graphene.String()

def resolve_prerreq_objects(self, context):
    prerrequisites = db_session.query(CoursePrerrequisites).all()
    return prerrequisites
