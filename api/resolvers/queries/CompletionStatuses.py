import graphene
from api.models.sessionHelper import get_session
from api.models.models import CompletionStatus
from os import path

class CompletionStatusObj(graphene.ObjectType):
    status = graphene.String()
    name = graphene.String()

def _resolve_completion_statuses(self, context):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)

    statuses = db_session.query(CompletionStatus).all()

    return statuses
