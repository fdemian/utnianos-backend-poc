import graphene
from api.models.models import ContribType, db_session #, UserActivation
from os import path

class ContribTypeObj(graphene.ObjectType):
      id = graphene.Int()
      name = graphene.String()

def resolve_contrib_objects(self, context):
    all_types = db_session.query(ContribType).all()
    return all_types
