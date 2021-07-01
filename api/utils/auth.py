import jwt
from datetime import datetime, timedelta

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
