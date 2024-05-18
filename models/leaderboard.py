#!/usr/bin/python
""" holds class Leaderboard """
from sqlalchemy import Column, String, Integer
from models.base_model import BaseModel, Base

class Leaderboard(BaseModel, Base):
    """Representation of a Leaderboard"""
    __tablename__ = 'leaderboard'
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    instagram = Column(String(255), nullable=True)
    facebook = Column(String(255), nullable=True)
    whatsapp = Column(String(255), nullable=True)
    twitter = Column(String(255), nullable=True)
    reports = Column(Integer, nullable=True, default=0)
    on_platform = Column(Integer, nullable=True, default=0)

    def __init__(self, *args, **kwargs):
        """initializes Leaderboard"""
        super().__init__(*args, **kwargs)
    
