# app/routes/ai.py
from flask import Blueprint, render_template

ai_bp = Blueprint(
    "ai",
    __name__,
    url_prefix="/ai"
)

@ai_bp.route("/")
def ai_home():
    """
    AI services overview.
    """
    return render_template("ai/index.html")


@ai_bp.route("/digital-twins")
def digital_twins():
    """
    Digital twin modelling and simulation.
    """
    return render_template("ai/digital_twins.html")


@ai_bp.route("/agent-based")
def agent_based():
    """
    Agent-based modelling and multi-agent systems.
    """
    return render_template("ai/agent_based.html")


@ai_bp.route("/simulation")
def simulation():
    """
    Large-scale system simulation and scenario analysis.
    """
    return render_template("ai/simulation.html")


@ai_bp.route("/automation")
def automation():
    """
    AI-driven business process automation.
    """
    return render_template("ai/automation.html")


@ai_bp.route("/agent_modeling")
def agent_modeling():
    """
    Agent-based modeling and multi-agent systems.
    """
    return render_template("ai/agent_modeling.html")