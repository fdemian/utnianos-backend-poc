import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.models import (
  ClassMaterial,
  Course,
  File,
  db_session
 )
from api.scripts.add_user import do_save_user
from os import path

class FileParam(graphene.InputObjectType):
   url = graphene.String()
   type = graphene.String()

class AddContribution(graphene.Mutation):

    ok = graphene.String()
    id = graphene.Int()

    class Arguments:
        title = graphene.String()
        description = graphene.String()
        types = graphene.String()
        course = graphene.String()
        files_list = graphene.List(FileParam)

    def mutate(self, info, title, description, types, course, files_list):

        try:
          course_obj = db_session.query(Course).filter(Course.name == course).one()
          course_material = ClassMaterial();
          course_material.name = title
          course_material.description = description
          course_material.course = course_obj
          course_material.contrib_types = types
          db_session.add(course_material)
          db_session.commit()
          cm_id = course_material.id

          for file in files_list:
              print(file.url)
              print(file.type)
              file_to_save = File()
              file_to_save.path = file.url
              file_to_save.type = file.type
              file_to_save.class_material_id = cm_id
              db_session.add(file_to_save)

          db_session.commit()

        except MultipleResultsFound:
           return AddContribution(ok=False, id=0)

        except NoResultFound:
           return AddContribution(ok=False, id=0)

        return AddContribution(
          ok=True,
          id=course_material.id
        )
