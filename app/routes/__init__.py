from flask import Flask

bp = Blueprint('main', __name__)

from app.routes import auth, trips, destinations


