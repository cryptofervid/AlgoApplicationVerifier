from app import app
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

if __name__ == '__main__':
    app.secret_key = os.getenv('SECRET_KEY')
    app.run()