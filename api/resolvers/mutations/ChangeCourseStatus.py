import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import CoursesStatus
from os import path

class ChangeCourseStatus(graphene.Mutation):

    ok = graphene.Boolean()
    course_id = graphene.Int()
    status_id = graphene.Int()

    class Arguments:
        course_id = graphene.Int()
        user_id = graphene.Int()
        status_id = graphene.Int()

    def mutate(self, info, course_id, user_id, status_id):
        config_file = '../../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        db_session = get_session(config_file_path)

        try:

          status_to_change = db_session.query(CoursesStatus).filter(
             CoursesStatus.course_id == course_id,
             CoursesStatus.user_id == user_id
          ).one()
          status_to_change.completion_id = status_id

          db_session.add(status_to_change)
          db_session.commit()

        except MultipleResultsFound:
           return ChangeCourseStatus(ok=False)

        except NoResultFound:
           return ChangeCourseStatus(ok=False)

        return ChangeCourseStatus(
           ok=True,
           course_id=course_id,
           status_id=status_id
        )
