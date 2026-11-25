from sqlalchemy.orm import Session

from Models.user_model import User
from Authentication.password import hash_password,verify_password
from Authentication.jwt import create_access_token


def register_user(db: Session, user_data):

    # Check whether email already exists
    existing_user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    if existing_user:
        return None

    # Hash the password
    hashed_password = hash_password(user_data.password)

    # Create new user
    new_user = User(
        name=user_data.name,
        email=user_data.email,
        phone=user_data.phone,
        password_hash=hashed_password
    )

    # Save user in database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Generate JWT token
    token = create_access_token(new_user.id)

    return new_user, token

def login_user(db: Session, user_data):

    # Find user by email
    user = db.query(User).filter(
        User.email == user_data.email
    ).first()

    # Check whether user exists
    if not user:
        return None

    # Verify password
    is_password_valid = verify_password(
        user_data.password,
        user.password_hash
    )

    if not is_password_valid:
        return None

    # Generate JWT token
    token = create_access_token(user.id)

    return user, token

def update_user_profile(db: Session, user, user_data):

    # Update name if provided
    if user_data.name is not None:
        user.name = user_data.name

    # Update phone if provided
    if user_data.phone is not None:
        user.phone = user_data.phone

    # Save changes to database
    db.commit()

    # Refresh user data
    db.refresh(user)

    return user