"""This Contains the models"""
from models.transaction import Transaction
from models.user import User
from models.leaderboard import Leaderboard
from models.messages import Message

class db_models:
    __classes = {"Transaction": Transaction, 
                 "User": User,
                 "Leaderboard": Leaderboard,
                 "Message": Message
                 }

    @classmethod
    def get_dict(cls):
        return cls.__classes

