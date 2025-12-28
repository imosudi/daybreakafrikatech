from flask import Blueprint, render_template

solutions_bp = Blueprint(
    "solutions",
    __name__,
    url_prefix="/solutions"
)

@solutions_bp.route("/", endpoint="index")
def index():
    return render_template("solutions/index.html")


@solutions_bp.route("/infrastructure/", endpoint="infrastructure")
def infrastructure():
    return render_template("solutions/infrastructure.html")


@solutions_bp.route("/networking/", endpoint="networking")
def networking():
    return render_template("solutions/networking.html")


@solutions_bp.route("/cloud/", endpoint="cloud")
def cloud():
    return render_template("solutions/cloud.html")


@solutions_bp.route("/software/", endpoint="software")
def software():
    return render_template("solutions/software.html")


@solutions_bp.route("/ai/", endpoint="ai")
def ai():
    return render_template("solutions/ai.html")


@solutions_bp.route("/security/", endpoint="security")
def security():
    return render_template("solutions/security.html")
