import graphene
from api.models.sessionHelper import get_session
from api.models.models import CareerPlan
from os import path

class CareerPlanObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()

def resolve_career_plan_objects(self, context):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    career_plans = db_session.query(CareerPlan).all()

    return career_plans
