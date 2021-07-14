import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import ClassMaterial, Course
from api.scripts.add_user import do_save_user
from os import path

class AddContribution(graphene.Mutation):

    ok = graphene.String()
    id = graphene.Int()

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        types = graphene.String()
        course = graphene.String()
        path = graphene.String(required=False)

    def mutate(self, info, title, description, types, course, **kwargs):
        config_file = '../../config.json'
        config_file_path = path.join(path.dirname(__file__), config_file)

        db_session = get_session(config_file_path)
        file_path = kwargs.get('path', None)

        try:
          course_obj = db_session.query(Course).filter(Course.name == course).one()
          course_material = ClassMaterial();
          course_material.name = title
          course_material.course = course_obj
          course_material.file_path = file_path
          course_material.contrib_types = ','.join(types)

          db_session.add(course_material)
          db_session.commit()

        except MultipleResultsFound:
           return AddContribution(ok=False, id=0)

        except NoResultFound:
           return AddContribution(ok=False, id=0)

        return AddContribution(
          ok=True,
          id=course_material.id
        )
