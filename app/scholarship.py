from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db import get_db

bp = Blueprint('scholarship', __name__, url_prefix='/scholarship')

@bp.route('/')
def index():
    db = get_db()
    scholarships = db.execute(
        'SELECT id, name, amount, deadline, status FROM scholarship ORDER BY deadline ASC'
    ).fetchall()
    return render_template('scholarship/index.html', scholarships=scholarships)

@bp.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        deadline = request.form['deadline']
        status = request.form['status']
        db = get_db()
        db.execute(
            'INSERT INTO scholarship (name, amount, deadline, status) VALUES (?, ?, ?, ?)',
            (name, amount, deadline, status)
        )
        db.commit()
        flash('Scholarship added successfully.')
        return redirect(url_for('scholarship.index'))
    return render_template('scholarship/create.html')
