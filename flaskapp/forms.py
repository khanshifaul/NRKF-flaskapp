from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField, BooleanField, DateField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
                           DataRequired(), Length(min=6)])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=6)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class AddStudentForm(FlaskForm):
    studentname = StringField('Student\'s Name', validators=[DataRequired()])
    fathername = StringField('Father\'s Name', validators=[DataRequired()])
    mothername = StringField('Mother\'s Name', validators=[DataRequired()])
    dateofbirth = DateField('Date of Birth', validators=[DataRequired()])
    sex = SelectField('Sex', validators=[DataRequired()], choices=[('male', 'Male'), ('female', 'Female')])
    bcertno = IntegerField('Birth Certificate No')
    # division = SelectField('division', choices=division, validators=[DataRequired()])
    district = StringField('District', validators=[DataRequired()])
    thana = StringField('Thana', validators=[DataRequired()])
    upazilla = StringField('Upazilla', validators=[DataRequired()])
    village = StringField('Village', validators=[DataRequired()])
    post = StringField('Post Office', validators=[DataRequired()])
    postcode = IntegerField('Postal Code', validators=[DataRequired()])
    submit = SubmitField('ADD')
