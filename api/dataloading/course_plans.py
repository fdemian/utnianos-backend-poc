import json
from os import path
from api.models.sessionHelper import get_session
from api.models.models import CoursesPlans

def get_db_session():
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    session_object = get_session(config_file_path)
    session = session_object()

    return session


def associate_course_plans(file):

    association_file = open(file)
    associations = json.load(association_file)
    session = get_db_session();

    code = associations['code']
    for course in associations['courses']:
        db_plan = CoursesPlans()
        db_plan.career_plan_code = code
        db_plan.course_code = course
        session.add(db_plan)

    session.commit()

if __name__ == '__main__':
    associate_course_plans()
