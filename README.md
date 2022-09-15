"# PollApi" \
API for user surveys

Task: [TASK](task.txt) 

Briefly: 
 * CRUD surveys and questions in them for administrators,
 * Passing through surveys (creating responses),
 * Viewing responses by user id.
 
Used:
 * **Django 2.2;**
 * **DjangoRestFramework;**
 * **JWT token;**
 * **sqlite3;**
 * **PostgreSQL;**
 * **Docker.**

API documentation (under development): [EMPTY](api.txt) \
Implemented in the project by internal url http://localhost:8000/docs/

Possible to work with internal sqlite database without docker:
 * Installing the virtual environment:\
`python -m venv env`.
 * Activating the environment:\
`env\Scripts\activate`.
 * Installing dependencies:\
\pip install -r requirements.txt
 * Running the application:\
`python manage.py runserver

Build a docker image and run it:\
`docker-compose up -d --build`.

Administrator login/password: \
`admin/admin

##TODO:
* documentation
* tests
* filling the database (saving to dump)
