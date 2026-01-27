from flask import Blueprint, render_template
import logging

import jinja2


errors_bp = Blueprint("errors", __name__)

# -------- 400 Errors --------

@errors_bp.app_errorhandler(400)
def bad_request(error):
    return render_template("errors/400.html"), 400


@errors_bp.app_errorhandler(403)
def forbidden(error):
    return render_template("errors/403.html"), 403


@errors_bp.app_errorhandler(404)
def not_found(error):
    return render_template("errors/404.html"), 404


# -------- 500 Errors --------

@errors_bp.app_errorhandler(500)
def internal_server_error(error):
    logging.exception("Unhandled exception occurred")
    return render_template("errors/500.html"), 500

@errors_bp.app_errorhandler(502)
def bad_gateway(error):
    return render_template("errors/502.html"), 502  


# -------- Jinja2 Errors --------
jinja2.exceptions.TemplateNotFound
@errors_bp.app_errorhandler(jinja2.exceptions.TemplateNotFound)
def template_not_found(error):
    logging.error(f"Template not found: {error}")
    return render_template("errors/404.html"), 404  