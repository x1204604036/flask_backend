from sqlalchemy import Column, Integer, String
from app.database import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), default="", comment="邮箱")
    password = Column(String(120))