try:
    import jwt
except ImportError:
    jwt = None

SECRET_KEY = "apibank_secret"


def TryConnectUser():
    if jwt:
        return jwt.encode({"status": "connected"}, SECRET_KEY, algorithm="HS256")
    return "token_jwt_placeholder"
    return True