from flask import request
from flask_babel import gettext
from .extensions import babel

# ✅ دالة مستقلة يمكن استيرادها
def get_locale():
    lang = request.args.get("lang")
    print("📥 lang param:", lang)
    if lang in ['de', 'en', 'ar']:
        return lang
    return request.accept_languages.best_match(['de', 'en', 'ar'])

def init_i18n(app):
    # ✅ اربطها هنا
    babel.locale_selector_func = get_locale

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    @app.context_processor
    def inject_translation():
        return dict(gettext=gettext)
