from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jwt import InvalidTokenError

from auth.schemas import Token
from auth.utils import encode_jwt, decode_jwt
from core.models import UserService

http_bearer = HTTPBearer()


# Создание токена для пользователя
def creation_token_for_user_service(
        user: UserService):
    #u_id = user_id if user_id else user.id
    #u_login = user_login if user_login else user.login

    jwt_payload = {
        "sub": str(user.id),
        "login": user.login
    }

    token = encode_jwt(jwt_payload)
    return Token(access_token=token, token_type="Bearer")


# Получение payload из токена
def get_current_token_payload(
        credentials: HTTPAuthorizationCredentials = Depends(http_bearer),
) -> dict:
    token: str = credentials.credentials
    try:
        payload = decode_jwt(
            token=token,
        )
    except InvalidTokenError as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"invalid token error",
        )
    return payload
