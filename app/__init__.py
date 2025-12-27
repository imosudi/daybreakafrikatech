# app/__init__.py
import os
from flask import Flask
from flask_moment import Moment
from config import Config
from app.extensions import close_db

# Blueprints
from app.routes.main import main_bp
from app.routes.solutions import solutions_bp
from app.routes.developer import developer_bp
from app.routes.ai import ai_bp
from app.routes.solution_finder import solution_finder_bp
from app.routes.errors import errors_bp

# Get the absolute path to the app directory
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
    template_folder=os.path.join(basedir, "templates"),
    static_folder=os.path.join(basedir, "static"))

app.config.from_object(Config)

moment = Moment(app)

# Register teardown
app.teardown_appcontext(close_db)

# Register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(solutions_bp, url_prefix="/solutions")
app.register_blueprint(developer_bp, url_prefix="/developer")
app.register_blueprint(ai_bp, url_prefix="/ai")
app.register_blueprint(solution_finder_bp, url_prefix="/solution-finder")
app.register_blueprint(errors_bp)
