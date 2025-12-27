# app/routes/solution_finder.py
from flask import Blueprint, render_template, request, jsonify
from app.extensions import get_db
import logging

solution_finder_bp = Blueprint(
    "solution_finder",
    __name__,
    url_prefix="/solution-finder"
)

# Mapping business needs to solutions
RECOMMENDATION_MAP = {
    "Secure Access Control": "Security Gateway & Identity Management",
    "5G Networking": "5G SA/NSA & MEC Deployment",
    "AI Modelling": "Agent-Based & Digital Twin Systems"
}
DEFAULT_RECOMMENDATION = "Custom Enterprise Technology Assessment"

# Configure logger
logger = logging.getLogger(__name__)


@solution_finder_bp.route("/", methods=["GET"])
def solution_finder_page():
    """
    Interactive solution finder page.
    """
    return render_template("solution_finder/index.html")


@solution_finder_bp.route("/analyze", methods=["POST"])
def analyze():
    """
    Analyze user business needs and return recommended solutions.
    Stores the inquiry in the database.
    """
    data = request.get_json(silent=True) or {}
    business_need = data.get("business_need", "").strip()

    recommendation = RECOMMENDATION_MAP.get(business_need, DEFAULT_RECOMMENDATION)

    # Persist inquiry
    try:
        db = get_db()
        db.execute(
            """
            INSERT INTO inquiries (business_need, recommended_solution)
            VALUES (?, ?)
            """,
            (business_need, recommendation)
        )
        db.commit()
    except Exception as e:
        logger.warning(f"Failed to save solution inquiry: {e}")

    return jsonify({
        "business_need": business_need,
        "recommendation": recommendation
    })


@solution_finder_bp.route("/assess", methods=["POST"])
def assess():
    """
    Endpoint for advanced solution assessment.
    Returns primary and secondary recommendations along with reasoning.
    """
    data = request.get_json(silent=True) or {}

    # Placeholder logic for advanced assessment
    recommendations = {
        "primary": "Custom Enterprise AI",
        "secondary": ["Identity & API Solutions", "Cloud Infrastructure"],
        "reasoning": "Based on your requirements for automation and scalability."
    }

    return jsonify(recommendations)
