# flask_sqlalchemy/app.py
from flask import Flask
from api.models.models import db_session
from api.models.schema import schema
from flask_graphql_auth import GraphQLAuth
from flask_graphql import GraphQLView
from api.utils.utils import parse_config_file
from uploads import upload_file, serve_file
from os import path

config_file = './config.json'
config_file_path = path.join(path.dirname(__file__), config_file)
settings = parse_config_file(config_file_path)

# App configuration.
app = Flask(__name__)
app.debug = True
app.config['UPLOAD_FOLDER'] = "/fileuploads"
app.config['SECRET_KEY'] = settings['jwt']['secret']
app.config["JWT_SECRET_KEY"] = settings['jwt']['secret']
app.config["JWT_REFRESH_TOKEN_EXPIRES"] = int(settings['jwt']['expiration'])
auth = GraphQLAuth(app)

@app.route('/api/uploads?name=<name>', methods=['GET', 'POST'])
def downloadFile(name):
    return serve_file(name)

@app.route('/api/uploads', methods=['POST'])
def uploadFile():
    return upload_file()

app.add_url_rule(
  '/graphql',
  view_func=GraphQLView.as_view(
  'graphql',
   schema=schema,
   graphiql=False,
   batch=True
  )
)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run()
