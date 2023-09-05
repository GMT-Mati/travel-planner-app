from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Load configuration from config.py
app.config,from_object('config')

# Initialize the database
db = SQLAlchemy(app)

from app import routes, models
