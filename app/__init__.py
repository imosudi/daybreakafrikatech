# app/__init__.py
import os
from flask import Flask, render_template
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


app.route("/contact")(lambda: "Contact Page")
'''app.route("/services")(lambda: "Services Page")
app.route("/careers")(lambda: "Careers Page")
app.route("/blog")(lambda: "Blog Page")
app.route("/privacy-policy")(lambda: "Privacy Policy Page")
app.route("/terms-of-service")(lambda: "Terms of Service Page")
app.route("/faqs")(lambda: "FAQs Page")
app.route("/testimonials")(lambda: "Testimonials Page")
app.route("/partners")(lambda: "Partners Page")
app.route("/resources")(lambda: "Resources Page")
app.route("/events")(lambda: "Events Page")
app.route("/support")(lambda: "Support Page")
app.route("/sitemap.xml")(lambda: "Sitemap XML")
app.route("/robots.txt")(lambda: "Robots TXT")
app.route("/dashboard")(lambda: "Dashboard Page")
app.route("/profile")(lambda: "Profile Page")
app.route("/settings")(lambda: "Settings Page")
app.route("/logout")(lambda: "Logout Page")
app.route("/login")(lambda: "Login Page")
app.route("/register")(lambda: "Register Page") 
'''