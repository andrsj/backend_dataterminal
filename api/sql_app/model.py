from sqlalchemy import Column, Integer, String


from api.sql_app.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(String, unique=True, index=True)
    session_token = Column(String(length=24), unique=True, index=True)
