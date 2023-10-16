## О проекте

Тестовое задание в Пикассо


## Built With

* [![Docker][docker.com]][Docker-url]
* [![MySQL][mysql.org]][mysql-url]
* [![Django][djangoproject.com]][Django-url]
* [![Python][Python.org]][Python-url]


## Endpoints:

    GET /storage/files/ - получение всех загруженных объектов

    POST /storage/upload/ - загрузка файла и асинхронная обработка в фоне в зависимости от типа файла
    
    Файл загружать через form-data по ключу file

    FLOWER находится на порту 5555, логин:пароль flower:flower


## Author
[Kuzmenko Nikita](https://github.com/Arahit0gami)


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

