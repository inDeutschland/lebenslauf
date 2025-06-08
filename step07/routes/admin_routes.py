from flask import Blueprint, render_template, request, redirect, url_for
from models.models import db, Section, Setting  

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



@admin_bp.route("/settings", methods=["GET", "POST"])
def manage_settings():
    error = None

    if request.method == "POST":
        try:
            for key, value in request.form.items():
                # نحاول تحويل القيمة إلى JSON أولًا للتحقق من صحتها
                import json
                json.loads(value.replace("'", '"'))  # محاولة قراءة التنسيق
                setting = Setting.query.filter_by(key=key).first()
                if setting:
                    setting.value = value
            db.session.commit()
            return redirect(url_for("admin.manage_settings"))
        except Exception as e:
            error = f"❌ Fehler im JSON-Format: {str(e)}"

    settings = Setting.query.all()
    return render_template("admin/settings.html", settings=settings, error=error)

