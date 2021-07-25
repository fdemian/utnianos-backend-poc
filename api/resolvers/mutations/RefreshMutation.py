import graphene
from flask_graphql_auth import (
    get_jwt_identity,
    create_access_token,
    mutation_jwt_refresh_token_required
)

class RefreshMutation(graphene.Mutation):
    class Arguments(object):
        refresh_token = graphene.String()

    new_token = graphene.String()

    @mutation_jwt_refresh_token_required
    def mutate(self):
        current_user = get_jwt_identity()
        return RefreshMutation(new_token=create_access_token(identity=current_user))
