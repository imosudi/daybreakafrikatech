from flask import Blueprint, render_template

ai_bp = Blueprint("ai", __name__)

@ai_bp.route("/")
def ai_home():
    return render_template("ai/index.html")

@ai_bp.route("/digital-twins")
def digital_twins():
    return render_template("ai/digital_twins.html")

@ai_bp.route("/agent-based")
def agent_based():
    return render_template("ai/agent_based.html")

@ai_bp.route("/simulation")
def simulation():
    return render_template("ai/simulation.html")
