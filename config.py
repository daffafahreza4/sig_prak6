import os 

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:Hidung135@localhost:5432/SIG_db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False