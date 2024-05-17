import string
import random

from flask import render_template, redirect, url_for, flash, abort

from . import app, db
from .models import URL_map
from .forms import URLForm


def get_unique_short_id(length: int = 6):
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits
    short_id = ""
    for _ in range(length):
        short_id += random.choice(alphabet)
    return short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URLForm()
    if form.validate_on_submit():
        original_link = form.original_link.data
        short_link = form.custom_id.data
        check_original_link = URL_map.query.filter_by(original=original_link).first()
        if check_original_link:
            flash("Уже есть данная длинная ссылка в базе")
            return render_template('index.html', form=form)
        if short_link:
            if URL_map.query.filter_by(short=short_link).first():
                flash("Уже есть данная такая короткая ссылка в базе")
                return render_template('index.html', form=form)
            else:
                new_short_link = short_link
        else:
            new_short_link = get_unique_short_id()
            while URL_map.query.filter_by(short=short_link).first():
                new_short_link = get_unique_short_id()
        url_map = URL_map(
            original=original_link,
            short=new_short_link
        )
        db.session.add(url_map)
        db.session.commit()
        flash("Ваша новая ссылка готова")
        new_link = url_for('index_view', _external=True) + new_short_link
        flash(new_link)
        return render_template('index.html', form=form)
    return render_template('index.html', form=form)


@app.route('/<string:short_link>', methods=['GET'])
def redirect_view(short_link):
    url_map = URL_map.query.filter_by(short=short_link).first()
    if url_map:
        return redirect(url_map.original)
    abort(404)
