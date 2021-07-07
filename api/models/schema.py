import graphene
from api.resolvers.AuthMutation import AuthMutation
from api.resolvers.RefreshMutation import RefreshMutation
from api.resolvers.User import UserObject, resolve_user_id
from api.resolvers.CreateUser import CreateUser
from flask_graphql_auth import query_header_jwt_required
from api.utils.auth import check_valid_headers
from flask import request
from werkzeug.exceptions import Unauthorized

class Query(graphene.ObjectType):
    user = graphene.Field(UserObject, id=graphene.Int())

    def resolve_user(self, context, id):
        auth_headers = request.headers.get('authorization')
        result = check_valid_headers(auth_headers)
        if(result is None):
            raise Unauthorized(description="Unauthorized user.")

        return resolve_user_id(self, context, id)

class Mutations(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    create_user = CreateUser.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
