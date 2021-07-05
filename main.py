# flask_sqlalchemy/app.py
from flask import Flask
from flask_graphql import GraphQLView
from api.models.models import db_session
from api.models.schema import schema
from flask_graphql_auth import GraphQLAuth

app = Flask(__name__)
app.debug = True

# TODO: get from config file.
app.config['SECRET_KEY'] = 'fdasdffsdasadffsda'
app.config["JWT_SECRET_KEY"] = "aafdjklklfdsaklfdsakjlfdsa"

auth = GraphQLAuth(app)

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
