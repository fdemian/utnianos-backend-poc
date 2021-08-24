import graphene
from api.models.sessionHelper import get_session
from api.models.models import CareerPlan, db_session
from api.resolvers.queries.Courses import CourseObj
from os import path

class CareerPlanObj(graphene.ObjectType):
    code = graphene.String()
    name = graphene.String()
    courses = graphene.List(graphene.NonNull(CourseObj))

def resolve_career_plan_objects(self, context):
    career_plans = db_session.query(CareerPlan).all()

    return career_plans

def _resolve_career_plan(self, context, id):
    career_plan = db_session.query(CareerPlan).filter(CareerPlan.code == id).one()

    return career_plan
