from flask import Flask # type: ignore
from routes import init_routes
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()


app = Flask(__name__)

# Initialize routes
init_routes(app)

if __name__ == '__main__':
    app.run(debug=True)
