from flask import Blueprint, render_template, request, jsonify
from app.extensions import get_db

solution_finder_bp = Blueprint("solution_finder", __name__)

@solution_finder_bp.route("/", methods=["GET"])
def solution_finder_page():
    return render_template("solution_finder/index.html")

@solution_finder_bp.route("/analyze", methods=["POST"])
def analyze_solution():
    data = request.get_json(silent=True) or {}

    business_need = data.get("business_need", "").strip()

    if business_need == "Secure Access Control":
        recommendation = "Security Gateway & Identity Management"
    elif business_need == "5G Networking":
        recommendation = "5G SA/NSA & MEC Deployment"
    elif business_need == "AI Modelling":
        recommendation = "Agent-Based & Digital Twin Systems"
    else:
        recommendation = "Custom Enterprise Technology Assessment"

    try:
        db = get_db()
        db.execute(
            """
            INSERT INTO inquiries (business_need, recommended_solution)
            VALUES (?, ?)
            """,
            (business_need, recommendation),
        )
        db.commit()
    except Exception:
        # Fail silently to avoid breaking user flow
        pass

    return jsonify({
        "business_need": business_need,
        "recommendation": recommendation
    })
