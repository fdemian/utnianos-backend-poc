import graphene

class FileObj(graphene.ObjectType):
    id = graphene.Int()
    path = graphene.String()
    type = graphene.String()
