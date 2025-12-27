# app/routes/solutions.py
from flask import Blueprint, render_template

solutions_bp = Blueprint(
    "solutions",
    __name__,
    url_prefix="/solutions"
)

@solutions_bp.route("/")
def index():
    """
    Solutions overview page.
    """
    return render_template("solutions/index.html")


@solutions_bp.route("/infrastructure")
def infrastructure():
    """
    IT Infrastructure solutions.
    """
    return render_template("solutions/infrastructure.html")


@solutions_bp.route("/networking")
def networking():
    """
    5G Networking and connectivity.
    """
    return render_template("solutions/networking.html")


@solutions_bp.route("/cloud")
def cloud():
    """
    Cloud computing solutions.
    """
    return render_template("solutions/cloud.html")


@solutions_bp.route("/software")
def software():
    """
    Enterprise software solutions.
    """
    return render_template("solutions/software.html")


@solutions_bp.route("/ai")
def ai():
    """
    AI solutions for enterprise automation and intelligence.
    """
    return render_template("solutions/ai.html")


@solutions_bp.route("/security")
def security():
    """
    Cybersecurity and resilience solutions.
    """
    return render_template("solutions/security.html")
