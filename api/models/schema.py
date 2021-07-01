import graphene
from graphene import relay, List
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from .models import (
 db_session,
 User as UserModel
)
from api.resolvers.Login import Login

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

schema = graphene.Schema(query=Query, mutation=Mutations)
