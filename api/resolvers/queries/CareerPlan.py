import graphene
from api.models.sessionHelper import get_session
from api.models.models import CareerPlan
from api.resolvers.queries.Courses import CourseObj
from os import path

class CareerPlanObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    courses = graphene.List(graphene.NonNull(CourseObj))

def resolve_career_plan_objects(self, context):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    career_plans = db_session.query(CareerPlan).all()

    return career_plans


def _resolve_career_plan(self, context, id):
    config_file = '../../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    career_plan = db_session.query(CareerPlan).filter(CareerPlan.id == id).one()
    
    return career_plan
