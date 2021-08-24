import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.models import ClassMaterial, Course, db_session
from api.resolvers.queries.Courses import CourseObj
from api.scripts.add_user import do_save_user
from os import path
from .Files import FileObj

class ClassMaterialObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    description = graphene.String()
    name = graphene.String()
    contrib_types = graphene.String()
    course = graphene.Field(CourseObj)
    files = graphene.List(graphene.NonNull(FileObj))

def resolve_class_materials(self, info):
    all_class_materials = db_session.query(ClassMaterial).all()
    return all_class_materials

def resolve_class_materials_id(self, info, id):
    try:
       class_material = db_session.query(ClassMaterial).filter(ClassMaterial.id == id).one()
       return class_material

    except MultipleResultsFound:
       return None

    except NoResultFound:
       return None
