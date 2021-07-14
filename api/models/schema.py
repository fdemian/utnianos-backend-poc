import graphene
from api.resolvers.AuthMutation import AuthMutation
from api.resolvers.RefreshMutation import RefreshMutation
from api.resolvers.User import UserObject, resolve_user_id
from api.resolvers.ContribTypes import ContribTypeObj, resolve_contrib_objects
from api.resolvers.AddContribution import AddContribution
from api.resolvers.Courses import CourseObj, resolve_course_objects
from api.resolvers.ClassMaterial import ClassMaterialObj, resolve_class_materials
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

    def resolve_class_materials(self,context):
        return resolve_class_materials(self, context)

class Mutations(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    create_user = CreateUser.Field()
    add_contrib = AddContribution.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
