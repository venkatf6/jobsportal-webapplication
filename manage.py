# manage.py


import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from project.server import app, db
from project.server.models import User


migrate = Migrate(app, db)
notifier = Manager(app)

# migrations
notifier.add_command('db', MigrateCommand)

@notifier.command
def create_db():
    """Creates the db tables."""
    db.create_all()


@notifier.command
def drop_db():
    """Drops the db tables."""
    db.drop_all()


@notifier.command
def create_admin():
    """Creates the admin user."""
    db.session.add(User(email='admin@jobsearch.com', password='admin', admin=True))
    db.session.commit()


@notifier.command
def create_data():
    """Creates sample data."""
    pass


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
