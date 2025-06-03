from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from .jwt import verifyAccessToken

oauth2Scheme = OAuth2PasswordBearer(tokenUrl="/user/auth")

def getCurrentUser(token: str = Depends(oauth2Scheme)):
    """
    Retrieves the current user based on the provided access token.

    Args:
        token (str): The access token to verify.

    Returns:
        dict: The user information if the token is valid.

    Raises:
        HTTPException: If the token is invalid or expired.
    """
    user = verifyAccessToken(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return user

def requiredRole(requiredRole: str):
    """
    Decorator to enforce role-based access control.

    Args:
        requiredRole (str): The role required to access the endpoint.

    Returns:
        function: The decorated function that checks the user's role.
    """
    def roleChecker(currentUser=Depends(getCurrentUser)):
        userRole = currentUser.get("role")
        if userRole != requiredRole:
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Forbidden: Insufficient permissions")
        return currentUser
    return roleChecker