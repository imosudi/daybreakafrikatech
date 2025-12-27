from flask import Blueprint, render_template

developer_bp = Blueprint("developer", __name__)

@developer_bp.route("/")
def developer_home():
    return render_template("developer/index.html")

@developer_bp.route("/identity-apis")
def identity_apis():
    return render_template("developer/identity_apis.html")

@developer_bp.route("/fullstack")
def fullstack():
    return render_template("developer/fullstack.html")

@developer_bp.route("/docs")
def api_docs():
    return render_template("developer/docs.html")

@developer_bp.route("/sandbox")
def sandbox():
    return render_template("developer/sandbox.html")
