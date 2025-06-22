from dotenv import load_dotenv
load_dotenv()  # <-- Add this at the very top

import os

print("Loaded DATABASE_URI:", os.getenv('DATABASE_URI'))  # Debug print

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False