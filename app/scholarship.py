# Name: Alexander Escobedo
# Class: INF601 - Advanced Programming in Python
# Project: Mini Project 3 - Scholarship Tracker

from flask import Blueprint, render_template, request, redirect, url_for, flash, g, Response
from app.db import get_db
from app.auth import login_required
from flask import abort
from datetime import datetime
import csv

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
        name = request.form['name'].strip()
        amount = request.form['amount']
        deadline = request.form['deadline']
        status = request.form['status']
        notes = request.form.get('notes', '')

        error = None
        if not name:
            error = 'Name is required.'
        try:
            amount = float(amount)
            if amount <= 0:
                error = 'Amount must be positive.'
        except ValueError:
            error = 'Amount must be a number.'
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            error = 'Deadline must be a valid date (YYYY-MM-DD).'

        if error:
            flash(error)
            return render_template('scholarship/create.html')

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
        name = request.form['name'].strip()
        amount = request.form['amount']
        deadline = request.form['deadline']
        status = request.form['status']
        notes = request.form.get('notes', '')

        error = None
        if not name:
            error = 'Name is required.'
        try:
            amount = float(amount)
            if amount <= 0:
                error = 'Amount must be positive.'
        except ValueError:
            error = 'Amount must be a number.'
        try:
            datetime.strptime(deadline, '%Y-%m-%d')
        except ValueError:
            error = 'Deadline must be a valid date (YYYY-MM-DD).'

        if error:
            flash(error)
            return render_template('scholarship/update.html', scholarship=scholarship)

        db = get_db()
        db.execute(
            'UPDATE scholarship SET name = ?, amount = ?, deadline = ?, status = ?, notes = ? '
            'WHERE id = ? AND user_id = ?',
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

@bp.route('/<int:id>')
@login_required
def detail(id):
    scholarship = get_scholarship(id)
    return render_template('scholarship/detail.html', scholarship=scholarship)

@bp.route('/stats')
@login_required
def stats():
    db = get_db()
    stats_data = db.execute(
        'SELECT status, COUNT(*) as count FROM scholarship WHERE user_id = ? GROUP BY status',
        (g.user['id'],)
    ).fetchall()
    total = db.execute(
        'SELECT COUNT(*) as total FROM scholarship WHERE user_id = ?', (g.user['id'],)
    ).fetchone()['total']
    return render_template('scholarship/stats.html', stats=stats_data, total=total)

@bp.route('/search', methods=('GET', 'POST'))
@login_required
def search():
    db = get_db()
    if request.method == 'POST':
        keyword = request.form.get('keyword', '').strip()
        status = request.form.get('status', '')
        query = 'SELECT * FROM scholarship WHERE user_id = ?'
        params = [g.user['id']]
        if keyword:
            query += ' AND name LIKE ?'
            params.append(f'%{keyword}%')
        if status and status != 'All':
            query += ' AND status = ?'
            params.append(status)
        query += ' ORDER BY deadline ASC'
    else:
        query = 'SELECT * FROM scholarship WHERE user_id = ? ORDER BY deadline ASC'
        params = [g.user['id']]
    scholarships = db.execute(query, params).fetchall()
    return render_template('scholarship/search.html', scholarships=scholarships)

@bp.route('/export')
@login_required
def export():
    db = get_db()
    scholarships = db.execute(
        'SELECT name, amount, deadline, status, notes FROM scholarship WHERE user_id = ? ORDER BY deadline ASC',
        (g.user['id'],)
    ).fetchall()
    if not scholarships:
        flash('You must create at least one scholarship before exporting.')
        return redirect(url_for('scholarship.index'))

    def generate_csv():
        yield 'Name,Amount,Deadline,Status,Notes\n'
        for s in scholarships:
            yield f"{s['name']},{s['amount']},{s['deadline']},{s['status']},{s['notes'] or ''}\n"

    return Response(generate_csv(), mimetype='text/csv',
                    headers={'Content-Disposition': 'attachment; filename=scholarships.csv'})
