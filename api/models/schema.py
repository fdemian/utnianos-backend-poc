import graphene
from api.resolvers.queries.Queries import Query
from api.resolvers.mutations.Mutations import Mutations
schema = graphene.Schema(query=Query, mutation=Mutations)
