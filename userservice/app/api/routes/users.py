from fastapi import APIRouter, HTTPException, Request
from ...schemas.user import UserRegister, UserLogin, TokenResponse, UserResponse
from ...services.user_service import UserService
from ...core.security import get_current_user, get_token_from_header
router = APIRouter(prefix="/users")


@router.post("/register", response_model=UserResponse)
async def register(user: UserRegister):
    try:
        return UserService.register(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin):
    token = UserService.authenticate(user.email, user.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}


@router.get("/me")
def read_users_me(request: Request):
    token = get_token_from_header(request)
    user = get_current_user(token)
    return user
