from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, title, body, created, author_id, username, like, dislike'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)

@bp.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO post (title, body, author_id, like, dislike)'
                ' VALUES (?, ?, ?, 0, 0)',
                (title, body, g.user['id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username, like, dislike'
        ' FROM post p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post


@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE post SET title = ?, body = ? WHERE id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))


# --- New Routes for Like / Dislike ---
@bp.route('/<int:id>/like', methods=('POST',))
@login_required
def toggle_like(id):
    post = get_post(id, check_author=False)
    if post['author_id'] != g.user['id']:
        db = get_db()
        new_like = 0 if post['like'] else 1
        db.execute(
            'UPDATE post SET like = ?, dislike = 0 WHERE id = ?',
            (new_like, id)
        )
        db.commit()
    return redirect(url_for('blog.index'))


@bp.route('/<int:id>/dislike', methods=('POST',))
@login_required
def toggle_dislike(id):
    post = get_post(id, check_author=False)
    if post['author_id'] != g.user['id']:
        db = get_db()
        new_dislike = 0 if post['dislike'] else 1
        db.execute(
            'UPDATE post SET dislike = ?, like = 0 WHERE id = ?',
            (new_dislike, id)
        )
        db.commit()
    return redirect(url_for('blog.index'))
