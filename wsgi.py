from app import app
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    app.config['SECRET_KEY'] = '4b45ca7595b5aced51da86e9e912949e6b3ca37bcc8d8f74'
    app.run()