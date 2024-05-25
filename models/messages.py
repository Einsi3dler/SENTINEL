#!/usr/bin/python
""" holds class Message """
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

class Message(BaseModel, Base):
    """Representation of a Message"""
    __tablename__ = 'messages'
    
    content = Column(String(1024), nullable=False)
    sender_id = Column(ForeignKey('users.id'), nullable=False)
    receiver_id = Column(ForeignKey('users.id'), nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    
    sender = relationship("User", foreign_keys=[sender_id])
    receiver = relationship("User", foreign_keys=[receiver_id])

    def __init__(self, *args, **kwargs):
        """initializes Message"""
        super().__init__(*args, **kwargs)
