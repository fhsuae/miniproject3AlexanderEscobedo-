# Name: Alexander Escobedo
# Class: INF601 - Advanced Programming in Python
# Project: Mini Project 3 - Scholarship Tracker

from flask import Blueprint, render_template, request, redirect, url_for, flash, g
from app.db import get_db
from app.auth import login_required
from flask import abort

bp = Blueprint('scholarship', __name__, url_prefix='/scholarship')


@bp.route('/')
@login_required
def index():
    db = get_db()
    scholarships = db.execute(
        'SELECT * FROM scholarship WHERE user_id = ? ORDER BY deadline ASC',
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
        notes = request.form.get('notes', '')
        db = get_db()
        db.execute(
            'INSERT INTO scholarship (user_id, name, amount, deadline, status, notes) VALUES (?, ?, ?, ?, ?, ?)',
            (g.user['id'], name, amount, deadline, status, notes)
        )
        db.commit()
        flash('Scholarship added successfully.')
        return redirect(url_for('scholarship.index'))
    return render_template('scholarship/create.html')


def get_scholarship(id):
    db = get_db()
    scholarship = db.execute(
        'SELECT * FROM scholarship WHERE id = ? AND user_id = ?', (id, g.user['id'])
    ).fetchone()
    if scholarship is None:
        abort(404)
    return scholarship


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    scholarship = get_scholarship(id)
    if request.method == 'POST':
        name = request.form['name']
        amount = request.form['amount']
        deadline = request.form['deadline']
        status = request.form['status']
        notes = request.form.get('notes', '')

        db = get_db()
        db.execute(
            'UPDATE scholarship SET name = ?, amount = ?, deadline = ?, status = ?, notes = ? WHERE id = ? AND user_id = ?',
            (name, amount, deadline, status, notes, id, g.user['id'])
        )
        db.commit()
        flash('Scholarship updated successfully.')
        return redirect(url_for('scholarship.index'))
    return render_template('scholarship/update.html', scholarship=scholarship)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    db = get_db()
    db.execute('DELETE FROM scholarship WHERE id = ? AND user_id = ?', (id, g.user['id']))
    db.commit()
    flash('Scholarship deleted successfully.')
    return redirect(url_for('scholarship.index'))
