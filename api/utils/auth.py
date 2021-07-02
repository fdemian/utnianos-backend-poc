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


def get_current_user(auth_headers, settings):
    
    if auth_headers is None:
        return None

    jwt_token = auth_headers.split("=")[1]
    jwt_secret = self.settings["jwt_secret"]
    jwt_algorhitm = self.settings["jwt_algorithm"]
    validated_user = validate_token(jwt_token, jwt_secret, jwt_algorhitm)

    if validated_user is None:
       return None

    # Perform additional validation on JWT claims.
    decoded_id = int(self.get_secure_cookie("user", value=validated_user["user_token"]))

    if decoded_id is None:
        return None

    return decoded_id
