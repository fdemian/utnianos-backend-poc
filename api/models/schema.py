import graphene
from api.resolvers.Login import Login
from api.resolvers.AuthMutation import AuthMutation
from api.resolvers.User import UserObject, resolve_user_id

"""
 class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    create_user = CreateUser.Field()
    protected_create_store = CreateStore.Field()
    refresh = RefreshMutation.Field() ## this is added
"""

class Query(graphene.ObjectType):
    user = graphene.Field(UserObject, id=graphene.Int())

    def resolve_user(self, context, id):
        return resolve_user_id(self, context, id)

class Mutations(graphene.ObjectType):
    login = Login.Field()
    auth = AuthMutation.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
