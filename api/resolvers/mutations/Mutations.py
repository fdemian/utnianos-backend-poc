import graphene

from .AuthMutation import AuthMutation
from .RefreshMutation import RefreshMutation
from .AddContribution import AddContribution
from .AddCareerPlan import AddCareerPlan
from .CreateUser import CreateUser

class Mutations(graphene.ObjectType):
    auth = AuthMutation.Field()
    refresh = RefreshMutation.Field()
    create_user = CreateUser.Field()
    add_contrib = AddContribution.Field()
    add_career_plan = AddCareerPlan.Field()
