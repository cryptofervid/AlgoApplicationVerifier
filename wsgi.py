from app import app
from dotenv import load_dotenv
import secrets

load_dotenv()

if __name__ == '__main__':
    app.secret_key = secrets.token_hex(24)
    app.run()