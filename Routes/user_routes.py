from fastapi import APIRouter, Depends, HTTPException, status,Response
from sqlalchemy.orm import Session

from database import get_db

from Schemas.user_schema import (
    UserRegister,
    UserLogin,
    UserProfileUpdate,
    ChangePassword
)

from Services.user_service import (
    register_user,
    login_user,
    update_user_profile,
    change_user_password
)

from Authentication.dependencies import get_current_user
from Models.user_model import User

router = APIRouter(
    prefix="/store/auth",
    tags=["Authentication"]
)


@router.post("/register", status_code=status.HTTP_201_CREATED)
def register(data: UserRegister, db: Session = Depends(get_db)):

    result = register_user(db, data)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered"
        )

    new_user, token = result

    return {
        "token": token,
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "phone": new_user.phone,
            "addresses": [],
            "createdAt": (
                new_user.created_at.isoformat()
                if new_user.created_at else None
            )
        }
    }
@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):

    result = login_user(db, data)

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    user, token = result

    return {
        "token": token,
        "user": {
            "id": user.id,
            "name": user.name,
            "email": user.email,
            "phone": user.phone,
            "addresses": [],
            "createdAt": (
                user.created_at.isoformat()
                if user.created_at else None
            )
        }
    }

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):

    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "phone": current_user.phone,
        "addresses": [],
        "createdAt": (
            current_user.created_at.isoformat()
            if current_user.created_at else None
        )
    }

@router.patch("/me")
def update_me(
    user_data: UserProfileUpdate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    updated_user = update_user_profile(
        db,
        current_user,
        user_data
    )

    return {
        "id": updated_user.id,
        "name": updated_user.name,
        "email": updated_user.email,
        "phone": updated_user.phone,
        "addresses": [],
        "createdAt": (
            updated_user.created_at.isoformat()
            if updated_user.created_at else None
        )
    }
@router.post(
    "/change-password",
    status_code=status.HTTP_204_NO_CONTENT
)
def change_password(
    password_data: ChangePassword,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    success = change_user_password(
        db,
        current_user,
        password_data
    )

    if not success:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Current password is incorrect"
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)