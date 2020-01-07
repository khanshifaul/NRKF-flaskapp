from datetime import datetime
from flaskapp import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    # student_added = db.relationship('Student', backref='user', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    father = db.Column(db.String(30))
    mother = db.Column(db.String(30))
    dateofbirth = db.Column(db.String(10))
    sex = db.Column(db.String(4))
    bcertno = db.Column(db.String(17))
    division = db.Column(db.String(30))
    district = db.Column(db.String(30))
    thana = db.Column(db.String(30))
    upazilla = db.Column(db.String(30))
    village = db.Column(db.String(30))
    post = db.Column(db.String(30))
    postcode = db.Column(db.String(4))
    # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Student('{self.name}')"
