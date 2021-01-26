"# PollApi" \
API для системы опросов пользователей

Задание: [TASK](task.txt) 

Кратко: 
 * CRUD опросов и вопросов в них для администраторов,
 * прохождение опросов (создание ответов),
 * просмотр ответов по user id.
 
Использовал:
 * **Django 2.2;**
 * **sqlite3;**
 * **PostgreSQL;**
 * **DjangoRestFramework;**
 * **Docker.**

Документация по API: [EMPTY](api.txt)

Возможна работа с внутренней базой sqlite без docker: \
`python manage.py runserver`

Сборка образа и запуск:\
`docker-compose up -d --build`

##TODO:
* документация
* тесты
* наполнение БД (сохрание в дамп)
