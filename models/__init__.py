#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("HBNB_TYPE_STORAGE")

if storage_t == "test_db":
    from models.engine.test_db_storage import Test_DBStorage
    storage = Test_DBStorage()
else:
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
storage.reload()
