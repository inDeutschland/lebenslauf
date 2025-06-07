import os
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

# مسار قاعدة البيانات من المجلد الأعلى
DB = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'flask_app.db'))

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    q = request.args.get('q', '').strip()
    if q:
        rows = conn.execute("""
            SELECT a.name AS attribute, e.example, e.is_manual, e.id
            FROM attributes a
            JOIN examples e ON a.id = e.attribute_id
            WHERE a.name LIKE ?
            ORDER BY e.is_manual DESC, a.name
        """, (f'%{q}%',)).fetchall()
    else:
        rows = conn.execute("""
            SELECT a.name AS attribute, e.example, e.is_manual, e.id
            FROM attributes a
            JOIN examples e ON a.id = e.attribute_id
            ORDER BY a.name
        """).fetchall()
    conn.close()
    return render_template('index.html', examples=rows, q=q)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    if request.method == 'POST':
        new_example = request.form['example']
        conn.execute("UPDATE examples SET example = ?, is_manual = 1 WHERE id = ?", (new_example, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    example = conn.execute("SELECT a.name AS attribute, e.example FROM examples e JOIN attributes a ON a.id = e.attribute_id WHERE e.id = ?", (id,)).fetchone()
    conn.close()
    return render_template('edit.html', example=example, id=id)

@app.route('/tools')
def tools():
    conn = get_db_connection()
    q = request.args.get('q', '').strip()
    if q:
        rows = conn.execute("""
            SELECT et.name, et.type, et.example, c.name as category, et.id
            FROM external_tools et
            LEFT JOIN categories c ON et.category_id = c.id
            WHERE et.name LIKE ?
            ORDER BY et.name
        """, (f'%{q}%',)).fetchall()
    else:
        rows = conn.execute("""
            SELECT et.name, et.type, et.example, c.name as category, et.id
            FROM external_tools et
            LEFT JOIN categories c ON et.category_id = c.id
            ORDER BY et.name
        """).fetchall()
    conn.close()
    return render_template('tools.html', tools=rows, q=q)

@app.route('/tools/edit/<int:id>', methods=['GET', 'POST'])
def edit_tool(id):
    conn = get_db_connection()
    if request.method == 'POST':
        new_example = request.form['example']
        conn.execute("UPDATE external_tools SET example = ?, is_manual = 1 WHERE id = ?", (new_example, id))
        conn.commit()
        conn.close()
        return redirect(url_for('tools'))
    tool = conn.execute("""
        SELECT et.name, et.type, et.example, c.name as category
        FROM external_tools et
        LEFT JOIN categories c ON et.category_id = c.id
        WHERE et.id = ?
    """, (id,)).fetchone()
    conn.close()
    return render_template('edit_tool.html', tool=tool, id=id)

@app.route('/add', methods=['GET', 'POST'])
def add_example():
    conn = get_db_connection()
    if request.method == 'POST':
        attribute_id = request.form['attribute_id']
        example = request.form['example']
        conn.execute("INSERT INTO examples (attribute_id, example, is_manual) VALUES (?, ?, 1)",
                     (attribute_id, example))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    attributes = conn.execute("SELECT id, name FROM attributes ORDER BY name").fetchall()
    conn.close()
    return render_template('add.html', attributes=attributes)

app.run(debug=True)
