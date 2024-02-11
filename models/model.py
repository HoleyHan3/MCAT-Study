from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import Table, Column, Integer, Numeric, String, ForeignKey, MetaData, DateTime
import sqlalchemy as sa
#import sqlalchemy.orm as so

class User(self):
    id = Column(Integer, primary_key=True) # primary keys are required by SQLAlchemy
    email = Column(String(100), unique=True)
    password = Column(String(100))
    name = Column(String(1000))

metadata = MetaData()

users = Table('users', metadata,
    Column('user_id', Integer(), primary_key=True),
    Column('username', String(15), nullable=False, unique=True), #nullable=false -> required
    Column('email_address', String(255), nullable=False),
    Column('phone', String(20), nullable=True), #nullable = True -> optional
    Column('password', String(25), nullable=False),
    Column('created_on', DateTime(), default=datetime.now), 
    Column('updated_on', DateTime(), default=datetime.now, onupdate=datetime.now))