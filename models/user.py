#!/usr/bin/python3
""" holds class User"""

import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash


class User(BaseModel, Base):
    """Representation of a user """
    
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    username = Column(String(128), nullable=False)

 

    def __init__(self, *args, **kwargs):
        """initializes user"""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """sets password encrypted with encryption"""
        if name == "password":
            value = generate_password_hash(value)
        super().__setattr__(name, value)

