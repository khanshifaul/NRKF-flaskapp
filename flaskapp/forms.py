from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Length, ValidationError, EqualTo, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6)])
    email = StringField('Email', validators=[DataRequired(), Length(min=4), Email])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    confirm_password = StringField('Confirm password', validators=[DataRequired(), EqualTo(password, 'message')])
    submit = SubmitField('Login')


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
    postcode = IntegerField('Postal Code', validators=[DataRequired(), Length(min=4)])
    submit = SubmitField('ADD')
