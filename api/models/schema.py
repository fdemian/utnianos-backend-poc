import graphene
from graphene import relay, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import (
 db_session,
 User as UserModel
)
from api.resolvers.Login import Login
from api.resolvers.AuthMutation import AuthMutation

"""
 class Mutation(graphene.ObjectType):
    auth = AuthMutation.Field()
    create_user = CreateUser.Field()
    protected_create_store = CreateStore.Field()
    refresh = RefreshMutation.Field() ## this is added
"""


class User(SQLAlchemyObjectType):
    class Meta:
        model = UserModel

class Query(graphene.ObjectType):
    users = List(User)

    def resolve_users(self, info):
        all_users = db_session().query(UserModel).all()
        return all_users

class Mutations(graphene.ObjectType):
    login = Login.Field()
    auth = AuthMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutations)
