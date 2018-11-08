from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'account'

    id = Column(String)
    username = Column(String, primary_key=True)
    password = Column(String)
    email = Column(String)

    def __repr__(self):
        return "<Account (username='%s')>" % (self.username)
