import graphene
from api.models.sessionHelper import get_session
from api.models.models import CompletionStatus, db_session
from os import path

class CompletionStatusObj(graphene.ObjectType):
    status = graphene.String()
    name = graphene.String()

def _resolve_completion_statuses(self, context):
    statuses = db_session.query(CompletionStatus).all()
    return statuses
