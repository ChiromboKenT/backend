
import os
from dotenv import load_dotenv
from flask import Flask # type: ignore
from flask_cors import CORS # type: ignore
from routes import init_routes

load_dotenv()


app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})  # Allow all origins for all routes
# Initialize routes
init_routes(app)


# ... your existing routes ...

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)