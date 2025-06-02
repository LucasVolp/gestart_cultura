from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

def createAccessToken(data: dict, expiresDelta: timedelta=None):
    """Creates a JWT access token with the provided data and expiration time.

    Args:
        data (dict): The payload data to include in the token.
        expiresDelta (timedelta, optional): The expiration time for the token. Defaults to 15 minutes.

    Returns:
        str: The generated JWT access token.
    """
    if expiresDelta is None:
        expiresDelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    toEncode = data.copy()
    expire = datetime.now(timezone.utc) + expiresDelta
    toEncode.update({"exp": expire})
    
    return jwt.encode(toEncode, SECRET_KEY, algorithm=ALGORITHM)

def verifyAccessToken(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None