import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import User, CareerPlan
from api.scripts.add_user import do_save_user
from os import path

class AddCareerPlan(graphene.Mutation):

    ok = graphene.Boolean()

    class Arguments:
        planId = graphene.Int()
        userId = graphene.Int()

    def mutate(self, info, planId, userId):
        config_file = '../../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)
        db_session = get_session(config_file_path)

        try:

          plan_to_add = db_session.query(CareerPlan).filter(CareerPlan.id == planId).one()
          user = db_session.query(User).filter(User.id == userId).one()
          user.career_plan = plan_to_add
          db_session.add(user)
          db_session.commit()

        except MultipleResultsFound:
           return AddCareerPlan(ok=False)

        except NoResultFound:
           return AddCareerPlan(ok=False)

        return AddCareerPlan(ok=True)
