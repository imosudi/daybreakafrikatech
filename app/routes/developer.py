from flask import Blueprint, render_template

developer_bp = Blueprint(
    "developer",
    __name__,
    url_prefix="/developer"
)

@developer_bp.route("/")
def index():
    """Developer portal home."""
    return render_template("developer/index.html")

@developer_bp.route("/identity-apis")
def identity_apis():
    """Identity and authentication APIs."""
    return render_template("developer/identity_apis.html")

@developer_bp.route("/fullstack")
def fullstack():
    """Full-stack development resources."""
    return render_template("developer/fullstack.html")

@developer_bp.route("/docs")
def docs():
    """API documentation."""
    return render_template("developer/docs.html")

@developer_bp.route("/sandbox")
def sandbox():
    """API sandbox environment."""
    return render_template("developer/sandbox.html")

@developer_bp.route("/guides")
def guides():
    """Integration and implementation guides."""
    return render_template("developer/guides.html")
