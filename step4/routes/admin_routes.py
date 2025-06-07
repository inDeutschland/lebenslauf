from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Section

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

@admin_bp.route("/sections", methods=["GET", "POST"])
def manage_sections():
    if request.method == "POST":
        for section_id, content in request.form.items():
            section = Section.query.get(int(section_id))
            if section:
                section.content = content
        db.session.commit()
        return redirect(url_for("admin.manage_sections"))

    sections = Section.query.all()
    return render_template("admin/sections.html", sections=sections)
