import graphene
from sqlalchemy.orm.exc import MultipleResultsFound, NoResultFound
from api.models.sessionHelper import get_session
from api.models.models import ClassMaterial, Course
from api.resolvers.Courses import CourseObj
from api.scripts.add_user import do_save_user
from os import path

class ClassMaterialObj(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    file_path = graphene.String()
    name = graphene.String()
    contrib_types = graphene.String()
    #course = graphene.ObjectType(CourseObj)

def resolve_class_materials(self, info):
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    db_session = get_session(config_file_path)
    all_class_materials = db_session.query(ClassMaterial).all()
    return all_class_materials
