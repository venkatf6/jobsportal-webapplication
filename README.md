### Quick Start

1. Install the requiremented modules/dependencies.

alembic==0.8.6
bcrypt==3.1.0
Flask
Flask-Bootstrap
Flask-DebugToolbar
Flask-Login
Flask-Script==2.0.5
Flask-SQLAlchemy==2.1
Flask-WTF==0.12
itsdangerous==0.24
Jinja2==2.8
Mako==1.0.4
MarkupSafe==0.23
pycparser==2.14
six==1.10.0
SQLAlchemy==1.0.14
visitor==0.1.3
Werkzeug==0.11.10
WTForms==2.1

### Set Environment Variables

```sh
$ export APP_SETTINGS="project.server.config.DevelopmentConfig"
```

### Create Database Models

```sh
$ python manage.py create_db
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py create_admin
$ python manage.py create_data
```

### Run the Application

```sh
$ python manage.py runserver
```

Application Address [http://localhost:5000/]


Testing
Testing2
Test7
