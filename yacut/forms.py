from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, Length


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[URL(message='Введите корректный URL')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, 16, message="Длина долдна быть от 1 до 16 символов")]
    )
    submit = SubmitField('Создать')
