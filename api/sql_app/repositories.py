import secrets
import string


from sqlalchemy.orm import Session


from api.sql_app import model


alphabet = string.ascii_letters + string.digits + '_-'


class UserRepository:

    @staticmethod
    def get_by_user_id(db: Session, user_id: str) -> model.UserModel:
        return db.query(model.UserModel).filter(model.UserModel.user_id == user_id).first()

    @staticmethod
    def add(db: Session, user_id: str) -> model.UserModel:
        db_user = model.UserModel(
            user_id=user_id,
            session_token=''.join(secrets.choice(alphabet) for _ in range(24))
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
