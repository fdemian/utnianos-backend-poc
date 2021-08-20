import json
from os import path
from api.models.sessionHelper import get_session
from api.models.models import Course

def get_db_session():
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    session_object = get_session(config_file_path)
    session = session_object()

    return session

def load_courses(file):
    course_file = open(file)
    courses = json.load(course_file)

    session = get_db_session();

    for course in courses:
        print(course)
        print(":::::::")
        db_course = Course()
        db_course.name = course['name']
        db_course.code = course['code']
        db_course.year = course['year']
        session.add(db_course)

    session.commit()



if __name__ == '__main__':
    load_courses()
