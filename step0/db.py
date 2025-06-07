# db.py
import sqlite3
import inspect
import flask
from flask import Flask

DB_PATH = "flask_app.db"
REBUILD_DB = True  # ✅ يمكنك تعيينه إلى False لاحقًا إذا لم ترغب في حذف الجداول

external_tools = [
    "Flask", "request", "session", "redirect", "url_for", "render_template", "abort",
    "g", "current_app", "Blueprint", "make_response", "jsonify", "Response",
    "Config", "escape", "flash", "get_flashed_messages"
]

tool_categories = {
    "Flask": "Core",
    "request": "Request",
    "session": "Session",
    "redirect": "Routing",
    "url_for": "Routing",
    "render_template": "Templating",
    "abort": "Error Handling",
    "g": "Globals",
    "current_app": "App Context",
    "Blueprint": "Structure",
    "make_response": "Response",
    "jsonify": "Response",
    "Response": "Response",
    "Config": "Configuration",
    "escape": "Security",
    "flash": "Messages",
    "get_flashed_messages": "Messages"
}

tool_examples = {
    "request": "name = request.args.get('name')",
    "session": "session['user'] = 'admin'",
    "redirect": "return redirect(url_for('home'))",
    "url_for": "url_for('index')",
    "render_template": "return render_template('index.html')",
    "abort": "abort(404)",
    "g": "g.user = current_user",
    "current_app": "current_app.logger.info('Hello')",
    "Blueprint": "bp = Blueprint('admin', __name__, url_prefix='/admin')",
    "make_response": "resp = make_response('Hello')",
    "jsonify": "return jsonify({'message': 'ok'})",
    "Response": "resp = Response('Hello', status=200)",
    "Config": "app.config['DEBUG'] = True",
    "escape": "escape('<script>')",
    "flash": "flash('Welcome!')",
    "get_flashed_messages": "get_flashed_messages()"
}

app = Flask(__name__)
filtered_attributes = [attr for attr in dir(app) if not attr.startswith("__")]

def guess_category(attr):
    name = attr.lower()
    if 'route' in name or 'url' in name or 'view' in name:
        return 'Routing'
    elif 'run' in name or 'wsgi' in name or 'client' in name:
        return 'Server'
    elif 'config' in name or 'secret' in name:
        return 'Configuration'
    elif 'jinja' in name or 'template' in name:
        return 'Templates'
    elif 'request' in name or 'response' in name or 'teardown' in name or 'context' in name:
        return 'Request Lifecycle'
    elif 'static' in name:
        return 'Static Files'
    elif 'session' in name:
        return 'Sessions'
    elif 'error' in name or 'exception' in name:
        return 'Error Handling'
    elif 'log' in name:
        return 'Logging'
    elif 'cli' in name or 'shell' in name:
        return 'CLI Tools'
    else:
        return 'Other'

def manual_example(attr):
    name = attr.lower()
    examples = {
        "run": "app.run(debug=True)",
        "route": "@app.route('/')\ndef home():\n    return 'Hello, World!'",
        "config": "app.config['DEBUG'] = True",
        "logger": "app.logger.info('Server started')",
        "get": "@app.get('/items')\ndef get_items():\n    return 'Items'",
        "post": "@app.post('/submit')\ndef submit():\n    return 'Submitted'",
        "template_folder": "app = Flask(__name__, template_folder='my_templates')",
        "static_folder": "app = Flask(__name__, static_folder='assets')",
        "before_request": "@app.before_request\ndef before():\n    print('Before request')",
        "after_request": "@app.after_request\ndef after(response):\n    print('After request')\n    return response",
        "errorhandler": "@app.errorhandler(404)\ndef not_found(e):\n    return 'Not Found', 404",
        "test_client": "client = app.test_client()\nresponse = client.get('/')",
        "url_for": "url_for('home')",
        "add_url_rule": "app.add_url_rule('/', 'index', lambda: 'Index')"
    }
    return examples.get(name)

def generate_example(attr):
    example = manual_example(attr)
    is_manual = 1 if example else 0
    if not example:
        example = f"# Placeholder example\napp.{attr}(...)"
    return example, is_manual

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
cur.execute("PRAGMA foreign_keys = ON;")

if REBUILD_DB:
    cur.executescript("""
    DROP TABLE IF EXISTS examples;
    DROP TABLE IF EXISTS attributes;
    DROP TABLE IF EXISTS categories;
    DROP TABLE IF EXISTS external_tools;
    """)

cur.executescript("""
CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS attributes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category_id INTEGER,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE IF NOT EXISTS examples (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    attribute_id INTEGER NOT NULL,
    example TEXT NOT NULL,
    is_manual INTEGER NOT NULL DEFAULT 0,
    FOREIGN KEY (attribute_id) REFERENCES attributes(id)
);

CREATE TABLE IF NOT EXISTS external_tools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT,
    category_id INTEGER,
    example TEXT,
    is_manual INTEGER DEFAULT 0,
    type TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);
""")

all_categories = set(guess_category(attr) for attr in filtered_attributes)
all_categories.update(tool_categories.values())

category_id_map = {}
for category in sorted(all_categories):
    cur.execute("INSERT OR IGNORE INTO categories (name) VALUES (?)", (category,))
    cur.execute("SELECT id FROM categories WHERE name = ?", (category,))
    category_id_map[category] = cur.fetchone()[0]
conn.commit()

for attr in filtered_attributes:
    category = guess_category(attr)
    category_id = category_id_map[category]
    cur.execute("INSERT INTO attributes (name, category_id) VALUES (?, ?)", (attr, category_id))
    attr_id = cur.lastrowid
    example, is_manual = generate_example(attr)
    cur.execute("INSERT INTO examples (attribute_id, example, is_manual) VALUES (?, ?, ?)", (attr_id, example, is_manual))
conn.commit()

# --- إدخال أدوات Flask الخارجية (تنفيذ نهائي بعد بناء كل شيء) ---
for name in external_tools:
    try:
        obj = getattr(flask, name)
    except AttributeError:
        obj = globals().get(name) or flask.__dict__.get(name)

    if obj is None:
        type_ = 'unresolved'
    elif inspect.isclass(obj):
        type_ = 'class'
    elif inspect.isfunction(obj):
        type_ = 'function'
    elif inspect.ismethod(obj):
        type_ = 'method'
    elif inspect.isbuiltin(obj):
        type_ = 'builtin'
    elif inspect.ismodule(obj):
        type_ = 'module'
    else:
        type_ = 'other'

    category = tool_categories.get(name, "Uncategorized")
    example = tool_examples.get(name, f"# No example yet for {name}")
    is_manual = 1 if name in tool_examples else 0

    category_id = category_id_map.get(category)
    if category_id is None:
        print(f"❌ تصنيف غير موجود: {category} — تخطٍ")
        continue

    print(f"✅ إدراج: {name} | التصنيف: {category} | النوع: {type_} | ID: {category_id}")
    cur.execute("""
        INSERT INTO external_tools (name, category, example, is_manual, type, category_id)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (name, category, example, is_manual, type_, category_id))
conn.commit()

cur.execute("SELECT COUNT(*) FROM external_tools")
print(f"\n📊 عدد الأدوات المُدخلة في external_tools: {cur.fetchone()[0]}")
cur.execute("SELECT COUNT(*) FROM attributes")
print(f"📊 عدد وكلاء app المُدخلة: {cur.fetchone()[0]}")

conn.close()
print("\n✅ تم بناء قاعدة البيانات بنجاح.")
