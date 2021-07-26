import graphene
from flask import request
from werkzeug.exceptions import Unauthorized
from api.utils.auth import check_valid_headers
from api.resolvers.queries.User import UserObject, resolve_user_id
from api.resolvers.queries.ContribTypes import ContribTypeObj, resolve_contrib_objects
from api.resolvers.queries.Courses import CourseObj, resolve_course_objects
from api.resolvers.queries.CareerPlan import (
    CareerPlanObj,
    resolve_career_plan_objects,
    _resolve_career_plan
)
from api.resolvers.queries.ClassMaterial import (
ClassMaterialObj,
resolve_class_materials,
resolve_class_materials_id
)

class Query(graphene.ObjectType):

    # Query fields.
    user = graphene.Field(UserObject, id=graphene.Int())
    contrib_types = graphene.List(graphene.NonNull(ContribTypeObj))
    courses = graphene.List(graphene.NonNull(CourseObj))
    class_materials = graphene.List(graphene.NonNull(ClassMaterialObj))
    class_material = graphene.Field(ClassMaterialObj, id=graphene.Int())
    career_plans = graphene.List(graphene.NonNull(CareerPlanObj))
    career_plan = graphene.Field(CareerPlanObj, id=graphene.Int())

    def resolve_user(self, context, id):
        auth_headers = request.headers.get('authorization')
        result = check_valid_headers(auth_headers)
        if(result is None):
            raise Unauthorized(description="Unauthorized user.")

        return resolve_user_id(self, context, id)

    def resolve_contrib_types(self, context):
        return resolve_contrib_objects(self, context)

    def resolve_courses(self, context):
        return resolve_course_objects(self, context)

    def resolve_career_plans(self, context):
        return resolve_career_plan_objects(self, context)

    def resolve_career_plan(self,context, id):
        return _resolve_career_plan(self, context, id)

    def resolve_class_materials(self,context):
        return resolve_class_materials(self, context)

    def resolve_class_material(self, info, id):
        return resolve_class_materials_id(self, info, id)
