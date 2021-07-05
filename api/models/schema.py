import graphene
from api.resolvers.AuthMutation import AuthMutation
from api.resolvers.RefreshMutation import RefreshMutation
from api.resolvers.User import UserObject, resolve_user_id
from flask_graphql_auth import query_header_jwt_required
from flask import request

def check_valid_headers(auth_headers):
    token = auth_headers.split(' ')[1]
    print(auth_headers)
    print(token)

class Query(graphene.ObjectType):
    user = graphene.Field(UserObject, id=graphene.Int())

    def resolve_user(self, context, id):
        auth_headers = request.headers.get('authorization')
        check_valid_headers(auth_headers)
        return resolve_user_id(self, context, id)

class Mutations(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
