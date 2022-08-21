from app import app
from dotenv import load_dotenv
import os

load_dotenv()

if __name__ == '__main__':
    SECRET_KEY = os.getenv('SECRET_KEY')
    app.config['SECRET_KEY'] = SECRET_KEY
    app.run()