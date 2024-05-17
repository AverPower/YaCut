<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/AverPower/YaMDB">
    <img src="yacut/static/img/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">YaCut - это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис</h3>

  <p align="center">
    Данный проект был написан в рамках 20 спринта обучения на курсе Python-разработчик от Яндекс.Практикума
    <br />
    <a href="https://github.com/AverPower/YaCut"><strong>Открыть код проекта »</strong></a>
    <br />
    <br />
  </p>
</div>

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone 
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/MacOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Запустить миграции

```
flask db migrate

flask db upgrade
```