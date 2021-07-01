# flask_sqlalchemy/app.py
from flask import Flask
from flask_graphql import GraphQLView
from api.models.models import db_session
from api.models.schema import schema, User

app = Flask(__name__)
app.debug = True

app.add_url_rule(
  '/graphql',
  view_func=GraphQLView.as_view(
    'graphql',
    schema=schema,
    graphiql=True
  )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
