import graphene
from api.resolvers.AuthMutation import AuthMutation
from api.resolvers.RefreshMutation import RefreshMutation
from api.resolvers.User import UserObject, resolve_user_id
from api.resolvers.ContribTypes import ContribTypeObj, resolve_contrib_objects
from api.resolvers.AddContribution import AddContribution
from api.resolvers.AddCareerPlan import AddCareerPlan
from api.resolvers.Courses import CourseObj, resolve_course_objects
from api.resolvers.CareerPlan import CareerPlanObj, resolve_career_plan_objects
from api.resolvers.ClassMaterial import (
ClassMaterialObj,
resolve_class_materials,
resolve_class_materials_id
)
from api.resolvers.CreateUser import CreateUser
from flask_graphql_auth import query_header_jwt_required
from api.utils.auth import check_valid_headers
from flask import request
from werkzeug.exceptions import Unauthorized

class Query(graphene.ObjectType):
    user = graphene.Field(UserObject, id=graphene.Int())
    contrib_types = graphene.List(graphene.NonNull(ContribTypeObj))
    courses = graphene.List(graphene.NonNull(CourseObj))
    class_materials = graphene.List(graphene.NonNull(ClassMaterialObj))
    class_material = graphene.Field(ClassMaterialObj, id=graphene.Int())
    career_plans = graphene.List(graphene.NonNull(CareerPlanObj))

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

    def resolve_class_materials(self,context):
        return resolve_class_materials(self, context)

    def resolve_class_material(self, info, id):
        return resolve_class_materials_id(self, info, id)

class Mutations(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    create_user = CreateUser.Field()
    add_contrib = AddContribution.Field()
    add_career_plan = AddCareerPlan.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
