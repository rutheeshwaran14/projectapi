from sqlalchemy import Column, Integer, String
from database import Base

class UserDB(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    role = Column(String(10), default="user")
    mobile_number=Column(String(10),unique=True)
