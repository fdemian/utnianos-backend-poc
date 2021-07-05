import jwt
from datetime import datetime, timedelta
from api.utils.utils import parse_config_file
from os import path

# Helper method (move?)
def get_user_token(user, context, expiration_time):

  jwt_settings = context['settings']['jwt']
  user_token = str(user["id"])
  expdate = datetime.utcnow() + timedelta(int(expiration_time))

  jwt_payload = {
    'user_token': user_token,
    'exp': expdate
  }

  jwt_token = jwt.encode(jwt_payload, jwt_settings["secret"], algorithm=jwt_settings["algorithm"])

  return jwt_token


def check_valid_headers(auth_headers):
    # No auth headers.
    if auth_headers is None:
        return False

    # Get JWT config from settings.
    config_file = '../../config.json'
    config_file_path = path.join(path.dirname(__file__), config_file)
    context = parse_config_file(config_file_path)
    jwt_settings = context['jwt']

    jwt_token = auth_headers.split(' ')[1]
    validated_user = validate_token(jwt_token, jwt_settings['secret'], jwt_settings['algorithm'])

    if validated_user is None:
        return None

    return validate_token


# Decode a JWT token and return the results.
def validate_token(jwt_token, secret, algorithm):
    try:
        if jwt_token is None:
            return None

        payload = jwt.decode(jwt_token, secret, algorithms=[algorithm])
        return payload

    except (jwt.DecodeError, jwt.ExpiredSignatureError):
        return None
