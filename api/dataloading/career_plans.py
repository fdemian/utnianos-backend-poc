import json
from os import path
from api.models.sessionHelper import get_session
from api.models.models import CareerPlan

def get_db_session():
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    session_object = get_session(config_file_path)
    session = session_object()

    return session

def load_career_plans(file):
    career_plans_file = open(file)
    plans = json.load(career_plans_file)

    session = get_db_session();

    for plan in plans:
        db_plan = CareerPlan()
        db_plan.name = plan['name']
        db_plan.code = plan['code']
        session.add(db_plan)

    session.commit()

if __name__ == '__main__':
    load_career_plans()
