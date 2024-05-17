import re

from flask import jsonify, request

from . import app, db
from .models import URL_map
from .error_handlers import InvalidAPIUsage
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def add_urlmap():
    if not request.data:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    data = request.get_json()
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)

    original_link = data.get('url')
    short_link = data.get('custom_id')
    check_original_link = URL_map.query.filter_by(original=original_link).first()
    if check_original_link:
        raise InvalidAPIUsage('Уже есть данная длинная ссылка в базе', 404)
    if short_link:
        if URL_map.query.filter_by(short=short_link).first():
            raise InvalidAPIUsage('Уже есть данная такая короткая ссылка в базе', 400)
        elif not re.match(r'^[A-Za-z0-9]+$', short_link) or len(short_link) > 16:
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
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
    new_link = f'http://{request.host}/{new_short_link}'
    return jsonify(
        {
            'url': original_link,
            'short_link': new_link
            }
        ), 201


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_urlmap(short_id):
    urlmap = URL_map.query.filter_by(short=short_id).first()
    if urlmap:
        return jsonify({'url': urlmap.original}), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)


@app.route('/api/<string:id>/', methods=['GET'])
def get_errors(id):
    raise InvalidAPIUsage('Неверный адрес', 404)
