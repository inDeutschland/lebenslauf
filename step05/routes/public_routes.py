from flask import Blueprint, render_template
from models.models import Section

public_bp = Blueprint("public", __name__)

@public_bp.route("/resume")
def resume():
    sections = Section.query.all()
    return render_template("public/resume.html", sections=sections)
