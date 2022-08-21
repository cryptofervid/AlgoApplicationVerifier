from app import app
from dotenv import load_dotenv
import secrets

load_dotenv()

if __name__ == '__main__':
    key = secrets.token_hex(24)
    app.config['SECRET_KEY'] = key
    app.run()