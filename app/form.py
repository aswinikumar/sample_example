from wtforms import Form, TextField, validators, SelectField, StringField, PasswordField, DateField, FileField, BooleanField
from wtforms.validators import ValidationError
from dbfunctions import *
class SigninForm(Form):
	username = StringField('user name', [validators.required(), validators.length(max=10)])
	password = PasswordField('password', [validators.required()]) 

class SignupForm(Form):
	firstname = StringField('firstname', [validators.required()])
	lastname = StringField('lastname', [validators.required()])
	email = TextField('Email', [validators.Length(min=6, max=120), validators.email()])
	birthday  = DateField('Your Birthday', format='%d-%m-%Y')
	gender = SelectField('Gender', choices=[('M', 'Male'),('FM', 'Female')])
	username = StringField('user name', [validators.required(), validators.length(max=10)])
	password = PasswordField('password', [validators.required()])
	addfile = FileField('urpic')
	accept_rules = BooleanField('I accept the site rules', [validators.Required()])
	def validate_email(form, field):
		emailid = checkfield('Users','email',field.data)
		if emailid:
        		raise ValidationError('Email id already exist')
	def validate_username(form, field):
		user_name = checkfield('Users','username',field.data)
		if user_name:
        		raise ValidationError('Username is already exist')

