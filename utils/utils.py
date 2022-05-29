import sqlalchemy
from sqlalchemy import column
import random
from os import times
import string

def row_to_dict(row):
    return {column: str(getattr(row, column)) for column in row.__table__.c.keys()}

def create_string():
    characters = string.ascii_letters + string.digits
    rand_string = ''.join(random.choice(characters) for i in range(8))
    return(rand_string)
