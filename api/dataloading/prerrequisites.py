import json
from os import path
from api.models.sessionHelper import get_session
from api.models.models import CoursePrerrequisites

def get_db_session():
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    session_object = get_session(config_file_path)
    session = session_object()

    return session

def load_prerrequisites(file):

    prerreq_files = open(file)
    prerreqs = json.load(prerreq_files)
    session = get_db_session();

    for prerreq in prerreqs:

        for courseReq in prerreq['courseRequisites']:
           db_prerreq = CoursePrerrequisites()
           db_prerreq.course_code = prerreq['code']
           db_prerreq.prerrequisite_code = courseReq['code']
           db_prerreq.completion_code = courseReq['status']
           db_prerreq.type = 'C'
           session.add(db_prerreq)

        for courseReq in prerreq['finalRequisites']:
           db_prerreq = CoursePrerrequisites()
           db_prerreq.course_code = prerreq['code']
           db_prerreq.prerrequisite_code = courseReq['code']
           db_prerreq.completion_code = courseReq['status']
           db_prerreq.type = 'F'
           session.add(db_prerreq)

        session.commit()

if __name__ == '__main__':
    load_prerrequisites()
