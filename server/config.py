from dotenv import load_dotenv
load_dotenv()  

import os

print("Loaded DATABASE_URI:", os.getenv('DATABASE_URI'))  

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False