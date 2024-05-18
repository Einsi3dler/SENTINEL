#!/usr/bin/python
""" holds class Amenity"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship

TRANSACTION_TYPES = ("deposit", "withdrawal", "transfer")

class Transaction(BaseModel, Base):
    """Representation of Amenity """
    
    __tablename__ = 'transactions'
    transaction_type = Column(Enum(*TRANSACTION_TYPES), nullable=False)
    sender_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    receiver_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Amenity"""
        super().__init__(*args, **kwargs)
