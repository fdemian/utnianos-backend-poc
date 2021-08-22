import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import (
  User,
  CareerPlan,
  CoursesStatus,
  CompletionStatus
)
from api.scripts.add_user import do_save_user
from os import path

class AddCareerPlan(graphene.Mutation):

    ok = graphene.Boolean()

    class Arguments:
        planId = graphene.String()
        userId = graphene.Int()

    def mutate(self, info, planId, userId):
        config_file = '../../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        db_session = get_session(config_file_path)

        try:

          plan_to_add = db_session.query(CareerPlan).filter(CareerPlan.code == planId).one()
          pending_status = db_session.query(CompletionStatus).filter(CompletionStatus.name == "Pendiente").one()
          user = db_session.query(User).filter(User.id == userId).one()
          user.career_plan = plan_to_add
          db_session.add(user)

          for course in plan_to_add.courses:
              status = CoursesStatus()
              status.user_id = user.id
              status.course_code = course.code
              status.completion_id = pending_status.id
              db_session.add(status)

          db_session.commit()

        except MultipleResultsFound:
           return AddCareerPlan(ok=False)

        except NoResultFound:
           return AddCareerPlan(ok=False)

        return AddCareerPlan(ok=True)
