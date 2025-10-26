from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from .db import get_db
from .auth import login_required

bp = Blueprint('scholarship', __name__, url_prefix='/scholarship')

@bp.route('/')
@login_required
def index():
    db = get_db()
    scholarships = db.execute(
        'SELECT * FROM scholarship WHERE user_id = ? ORDER BY deadline',
        (g.user['id'],)
    ).fetchall()
    return render_template('scholarship/index.html', scholarships=scholarships)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        deadline = request.form['deadline']
        status = request.form['status']
        notes = request.form['notes']
        error = None

        if not name:
            error = 'Name is required.'

        if error:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO scholarship (user_id, name, amount, deadline, status, notes) '
                'VALUES (?, ?, ?, ?, ?, ?)',
                (g.user['id'], name, amount, deadline, status, notes)
            )
            db.commit()
            return redirect(url_for('scholarship.index'))

    return render_template('scholarship/create.html')
