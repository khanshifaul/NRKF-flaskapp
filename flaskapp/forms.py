from flaskapp import app, bcrypt, db
from flaskapp.models import User, Student
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=6)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=6)])
    email = StringField('Email', validators=[
                        DataRequired(), Length(min=4), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirm password', validators=[
        DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter(User.username == username.data).first()
        if user is not None:
            raise ValidationError("A user with that username already exists")

    def validate_email(self, email):
        email = User.query.filter(User.email == email.data).first()
        if email is not None:
            raise ValidationError("A user with that email already exists")

    def get_password_hash(self):
        self.pw_hash = bcrypt.generate_password_hash(self.password.data)

    def register(self):
        u = User(username=self.username.data,
                 email=self.email.data, password=bcrypt.generate_password_hash(self.password.data))
        db.session.add(u)
        db.session.commit()


class AddStudentForm(FlaskForm):
    studentname = StringField('Student\'s Name', validators=[DataRequired()])
    fathername = StringField('Father\'s Name', validators=[DataRequired()])
    mothername = StringField('Mother\'s Name', validators=[DataRequired()])
    dateofbirth = DateField('Date of Birth', validators=[DataRequired()])
    sex = SelectField('Sex', validators=[DataRequired()], choices=[
                      ('male', 'Male'), ('female', 'Female')])
    bcertno = IntegerField('Birth Certificate No')
    # division = SelectField('division', choices=division, validators=[DataRequired()])
    district = StringField('District', validators=[DataRequired()])
    thana = StringField('Thana', validators=[DataRequired()])
    upazilla = StringField('Upazilla', validators=[DataRequired()])
    village = StringField('Village', validators=[DataRequired()])
    post = StringField('Post Office', validators=[DataRequired()])
    postcode = IntegerField('Postal Code', validators=[
                            DataRequired(), Length(min=4)])
    submit = SubmitField('ADD')
