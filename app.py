

from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from routes import init_routes

load_dotenv()


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes
# Initialize routes
init_routes(app)


# ... your existing routes ...

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)