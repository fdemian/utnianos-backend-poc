import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.models import CoursesStatus, db_session
from os import path

class ChangeCourseStatus(graphene.Mutation):

    ok = graphene.Boolean()
    course_code = graphene.String()
    status_code = graphene.String()

    class Arguments:
        course_code = graphene.String()
        user_id = graphene.Int()
        status_code = graphene.String()

    def mutate(self, info, course_code, user_id, status_code):
        try:

          status_to_change = db_session.query(CoursesStatus).filter(
             CoursesStatus.course_code == course_code,
             CoursesStatus.user_id == user_id
          ).one()
          status_to_change.completion_code = status_code

          db_session.add(status_to_change)
          db_session.commit()

        except MultipleResultsFound:
           return ChangeCourseStatus(ok=False)

        except NoResultFound:
           return ChangeCourseStatus(ok=False)

        return ChangeCourseStatus(
           ok=True,
           course_code=course_code,
           status_code=status_code
        )
