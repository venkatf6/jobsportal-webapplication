import datetime

from project.server import app, db, bcrypt


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, admin=False):
        self.email = email
        self.password = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        )
        self.registered_on = datetime.datetime.now()
        self.admin = admin

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
    
    def get_email(self):
        return self.email

    def __repr__(self):
        return '<User {0}>'.format(self.email)

class Profile(db.Model):

    __tablename__ = "profiles"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    phonenumber = db.Column(db.String(255),unique=True, nullable=False)
    zipcode = db.Column(db.String(255),unique=False, nullable=False)
    skillset = db.Column(db.String(255),unique=False, nullable=False)
    notifications = db.Column(db.String(255), nullable=False, default=False)
    created_on = db.Column(db.DateTime, nullable=False)

    #email, phonenumber, zipcode, skillset, notifications, created_on
    def __init__(self, email, phonenumber,zipcode,skillset,notifications,admin=False):
        self.email = email
        self.phonenumber = phonenumber
        self.created_on = datetime.datetime.now()
        self.zipcode = zipcode
        self.skillset = skillset
        self.notifications = notifications

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_email(self):
        return '<Profile {0}>'.format(self.email)

    def __repr__(self):
        return '<Profile {0}>'.format(self.email)

    


