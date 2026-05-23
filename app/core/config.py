import os
from dotenv import load_dotenv


load_dotenv()

class Settings:
    PROJECT_NAME = "Car Price Prediction API"
    API_KEY = os.getenv("API_KEY", "demo-key") 
    JWT_SECRET = os.getenv("JWT_SECRET", "secret-key")
    REDIS_URL = os.getenv("redis_url", "redis://localhost:6379")
    JWT_ALGORITHM = "HS256"
    MODEL_PATH = "app/models/model.pkl"
    

settings = Settings()    


