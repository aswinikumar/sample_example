from settings import *
import pymongo
from pymongo import MongoClient

# form.pymong

class SigninForm(Form):
        username = StringField('user name', [validators.required(), validators.length(max=10)])
        password = PasswordField('password', [validators.required()]) 

class SignupForm(Form):
        firstname = StringField('firstname', [validators.required()])
        lastname = StringField('lastname', [validators.required()])
        email = TextField('Email', [validators.Length(min=6, max=120), validators.email()])
        birthday  = DateField('Your Birthday', format='%d-%m-%Y')
        gender = SelectField('Gender', choices=[('Male', 'Male'),('Female', 'Female')])
        username = StringField('user name', [validators.required(), validators.length(min=4, max=10)])
        password = PasswordField('password', [validators.required()])
        accept_rules = BooleanField('I accept the site rules', [validators.Required()])
        def validate_email(form, field):
                emailid = checkfield('Users','email',field.data)
                if emailid:
                        raise ValidationError('Email id already exist')
        def validate_username(form, field):
                user_name = checkfield('Users','username',field.data)
                if user_name:
                        raise ValidationError('Username is already exist')


# end form mongo







# connect to database
def dbconnect() :
        
        client = MongoClient()
	db = client[databasename]
	return db

# To save the array into the collection 
def save_collection(collection,arr):

	db = dbconnect()
        coll = db[collection]
        data = coll.insert(arr)
        return data
      
# Updating a document in collection(old doc is replaced by new doc) and inserting if nothing there
def update_collection(collection,arr,ary):
      
	db = dbconnect()
        coll = db[collection]
        data = coll.update(arr,ary,upsert = True )
        return data

# To find the one array(first array from all the resulted arrays) from the collection
def find_one_in_collection(collection,arr):

	db = dbconnect()
        coll = db[collection]
        result = coll.find_one(arr)
        return result

# To Check Username or Email etc 
def checkfield(collection,field,value):
      
	db = dbconnect()
        coll = db[collection]
	checkarray = {field : value}
        checkresult = coll.find_one(checkarray)
        return checkresult

# find all the arrays in collection           
def find_all_in_collection(collection):
      
	db = dbconnect()
        coll = db[collection]
        cursor = coll.find()
        result = [item for item in cursor]
        return result

# find all the arrays in collection then return a particular field of all the docs
def find_all_and_filter(collection,arr):
     
	db = dbconnect()
        coll = db[collection]
        cursor = coll.find({},arr)
        result = [item for item in cursor]
        return result

# find all the arrays in collection then return arrays containing that particular arr
def find_in_collection(collection,arr):
      
	db = dbconnect()
        coll = db[collection]
        cursor = coll.find(arr)
        result = [item for item in cursor]
        return result
# find all the arrays in collection then return arrays containing that particular arr and sort by asc or desc
# sort_arr should give like this sort_arr = [("field",1)] 
def find_in_collection_sort(collection,arr,sort_arr):
      
	db = dbconnect()
        coll = db[collection]
        cursor = coll.find(arr).sort(sort_arr)
        result = [item for item in cursor]
        return result
 

   




