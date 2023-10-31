## О проекте

Тестовое задание в Пикассо


## Built With

* [![Docker][docker.com]][Docker-url]
* [![Python][Python.org]][Python-url]
* [![MySQL][mysql.org]][mysql-url]
* [![Django][djangoproject.com]][Django-url]
* [![Celery][docs.celeryq.dev]][celery-url]
* [![Redis][redis.io]][redis-url]


## Endpoints:

    GET /storage/files/ - получение всех загруженных объектов

    POST /storage/upload/ - загрузка файла и асинхронная обработка в фоне в зависимости от типа файла
    
    Файл загружать через form-data по ключу file, стоит ограничение на размер до 10мб

    FLOWER находится на порту 5555, логин:пароль flower:flower


## По заданию:
    Создал два разных docker-compose файла и "настройки" к ним.
    При первом запуске необходимо будет выполнить команды в терминале
    1) docker exec my-app /bin/bash -c "python manage.py migrate"
    2) docker exec my-app /bin/bash -c "python manage.py collectstatic"

Вопрос: Опишите, как изменится архитектура, если мы ожидаем большую нагрузку.</p>
1) Если говорить про celery, то можно добавить больше воркеров и увеличить количество паралельных
задач, которые может обрабатывать каждый воркер. Сейчас на одном воркере стоит одновременно 5 задач
2) Как вариант масштабировать приложение горизонтально (добавляя больше серверов) или вертикально (добавляя больше ресурсов на один сервер)

    

## Author
[Kuzmenko Nikita](https://github.com/arahitogami)

## P.S.
На заметку тем, кто будет смотреть это тестовое задание. 
Обратной связи от компании (Code Review) не поступало, поэтому я не знаю, насколько хорошо или плохо было выполнено задание.

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[djangoproject.com]: https://img.shields.io/badge/Django-4.2.6-green?style=plastic&logo=Django
[Django-url]: https://www.djangoproject.com/
[Python.org]: https://img.shields.io/badge/Python-3.11.0-green?style=plastic&logo=python
[Python-url]: https://python.org
[mysql.org]: https://img.shields.io/badge/MySQL-latest-green?style=plastic&logo=MySQL
[mysql-url]: https://www.mysql.com/
[docker.com]: https://img.shields.io/badge/Docker--compose-3.8-green?style=plastic&logo=docker
[Docker-url]: https://docker.com
[docs.celeryq.dev]: https://img.shields.io/badge/Celery-5.3.4-green?style=plastic&logo=celery&logoColor=green
[celery-url]: https://docs.celeryq.dev
[redis.io]: https://img.shields.io/badge/Redis-4.6.0-green?style=plastic&logo=redis
[redis-url]: https://redis.io/
