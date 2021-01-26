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

Документация по API: [EMPTY](api.txt) \
Реализована в проекте по внутреннему url http://localhost:8000/docs/

Возможна работа с внутренней базой sqlite без docker: \
 * Установка виртуального окружения:\
`python -m venv env`\
 * Активация окружения:\
`env\Scripts\activate`\
 * Установка зависимостей:\
`pip install -r requirements.txt`\
 * Запуск приложения:\
`python manage.py runserver`

Сборка образа docker и запуск:\
`docker-compose up -d --build`

##TODO:
* документация
* тесты
* наполнение БД (сохрание в дамп)
