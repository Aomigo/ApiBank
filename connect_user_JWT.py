import jwt
from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from user import User

secret_key = 'very_secret_key'
algorithm = 'HS256'

bearer_scheme = HTTPBearer()

def get_user(authorization: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    try:
        # Create the payload the added algorithms parameter here:
        payload = jwt.decode(authorization.credentials, secret_key, algorithms=[algorithm])
        return payload
    except jwt.PyJWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")


def generate_token(user: User):
    # Id and name
    payload = {"sub": user.id, "username": user.getUsername()}
    return jwt.encode(payload, secret_key, algorithm=algorithm)
