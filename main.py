# flask_sqlalchemy/app.py
from flask import Flask
from flask_graphql import GraphQLView
from api.models.models import db_session
from api.models.schema import schema
from flask_graphql_auth import GraphQLAuth
from api.utils.utils import parse_config_file
from os import path

app = Flask(__name__)
app.debug = True


config_file = './config.json'
config_file_path = path.join(path.dirname(__file__), config_file)
settings = parse_config_file(config_file_path)

# TODO: get from config file.
app.config['SECRET_KEY'] = settings['jwt']['secret']
app.config["JWT_SECRET_KEY"] = settings['jwt']['secret']
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = int(settings['jwt']['expiration'])
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
