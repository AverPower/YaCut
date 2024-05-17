from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, Length, DataRequired, Optional, Regexp


class URLForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            URL(message='Введите корректный URL'),
            DataRequired(message='Обязательное поле'),
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Length(1, 16, message="Длина должна быть от 1 до 16 символов"),
            Optional(),
            Regexp(r'^[A-Za-z0-9]+$', message="Предлагаемый вариант должен состоять из латинских букв и цифр")]
    )
    submit = SubmitField('Создать')
