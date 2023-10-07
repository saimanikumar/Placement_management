import json
from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from pymongo import MongoClient
from passlib.hash import pbkdf2_sha256
from flask_cors import CORS
from flask import jsonify
from bson import json_util

from flask_restful import Resource, reqparse
from pymongo import MongoClient
from PIL import Image
import io

import smtplib
from email.message import EmailMessage



from flask_jwt_extended import (
    create_access_token,
    jwt_required,
    get_jwt_identity,
)
from flask_restful import Resource
import os
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from pymongo.server_api import ServerApi
import werkzeug

app = Flask(__name__)


from flask import Flask,render_template
from flask_mail import Mail,Message



# app.config['SECRET_KEY'] = "tsfyguaistyatuis589566875623568956"

# app.config['MAIL_SERVER'] = "smtp.googlemail.com"

# app.config['MAIL_PORT'] = 587

# app.config['MAIL_USE_TLS'] = True


# mail = Mail(app)


app.config['JWT_SECRET_KEY'] = 'ssssrsssrssrssr'
jwt = JWTManager(app)

api = Api(app)
CORS(app)

# MongoDB configuration
client = MongoClient('y
connection URL', server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)


db = client['placement_management']
students_collection = db['students']
department_heads_collection = db['department_heads']
admins_collection = db['admins']

placements_collection = db['placements']
images = db['images']

# Request parser for user registration and login
user_register_parser = reqparse.RequestParser()
user_register_parser.add_argument('email', required=True, help='Email is required.')
user_register_parser.add_argument('password', required=True, help='Password is required.')
user_register_parser.add_argument('name', required=True, help='Student name is required.')
user_register_parser.add_argument('role', required=True, help='Role is required.')

user_register_parser.add_argument('student_id', help='Student ID is required.')
user_register_parser.add_argument('department_id', help='Student ID is required.')
user_register_parser.add_argument('admin_id', help='Student ID is required.')

st_parser = reqparse.RequestParser()

st_parser.add_argument('student_id')


user_login_parser = reqparse.RequestParser()
user_login_parser.add_argument('email', required=True, help='Email is required.')
user_login_parser.add_argument('password', required=True, help='Password is required.')

details_parser = reqparse.RequestParser()
details_parser.add_argument('student_id', required=True, help='Student ID is required.')
details_parser.add_argument('department_id', required=True, help='department_id is required.')
details_parser.add_argument('company_name', required=True, help='company_name is required.')
details_parser.add_argument('package', required=True, help='package is required.')
details_parser.add_argument('year', required=True, help='year is required.')


class StudentRegisterResource(Resource):
    def post(self):
        data = user_register_parser.parse_args()
        email = data.get('email')
        password = data.get('password')
        student_id = data.get('student_id')
        name = data.get('name')
        role = data.get('role')

        # Check if the email already exists
        existing_user = students_collection.find_one({'email': email})
        if existing_user:
            return {"error": "User already exists"}, 400

        # Hash the password before storing it
        hashed_password = pbkdf2_sha256.hash(password)

        # Create the user document
        user_data = {
            'email': email,
            'password': hashed_password,
            'student_id': student_id,
            'name': name,
            'role': role
        }

        # Insert the user data into MongoDB
        students_collection.insert_one(user_data)

        # Generate a JWT token for the user
        access_token = create_access_token(identity=email)

        return {
            'access_token': access_token,
            'role': role
        }, 200

class StudentLoginResource(Resource):
    def post(self):
        data = user_login_parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        # Retrieve the user document from MongoDB
        user_data = students_collection.find_one({'email': email})

        if user_data and pbkdf2_sha256.verify(password, user_data['password']):
            # Password is correct, generate a JWT token
            access_token = create_access_token(identity=email)
            return {
                'access_token': access_token,
                'role': user_data["role"],
                'id': user_data["student_id"]
            }, 200
        else:
            return {'error': 'Invalid credentials'}, 401

class DepartmentRegisterResource(Resource):
    def post(self):
        data = user_register_parser.parse_args()
        email = data.get('email')
        password = data.get('password')
        department_id = data.get('department_id')
        name = data.get('name')
        role = data.get('role')

        # Check if the email already exists
        existing_user = department_heads_collection.find_one({'email': email})
        if existing_user:
            return {"error": "User already exists"}, 400

        # Hash the password before storing it
        hashed_password = pbkdf2_sha256.hash(password)

        # Create the user document
        user_data = {
            'email': email,
            'password': hashed_password,
            'department_id': department_id,
            'name': name,
            'role': role
        }

        # Insert the user data into MongoDB
        department_heads_collection.insert_one(user_data)

        # Generate a JWT token for the user
        access_token = create_access_token(identity=email)

        return {
            'access_token': access_token,
            'role': role
        }, 200

class DepartmentLoginResource(Resource):
    def post(self):
        data = user_login_parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        # Retrieve the user document from MongoDB
        user_data = department_heads_collection.find_one({'email': email})

        if user_data and pbkdf2_sha256.verify(password, user_data['password']):
            # Password is correct, generate a JWT token
            access_token = create_access_token(identity=email)
            return {
                'access_token': access_token,
                'role': user_data["role"],
                'id': user_data["department_id"]
            }, 200
        else:
            return {'error': 'Invalid credentials'}, 401

class AdminRegisterResource(Resource):
    def post(self):
        data = user_register_parser.parse_args()
        email = data.get('email')
        password = data.get('password')
        admin_id = data.get('admin_id')
        name = data.get('name')
        role = data.get('role')

        # Check if the email already exists
        existing_user = admins_collection.find_one({'email': email})
        if existing_user:
            return {"error": "User already exists"}, 400

        # Hash the password before storing it
        hashed_password = pbkdf2_sha256.hash(password)

        # Create the user document
        user_data = {
            'email': email,
            'password': hashed_password,
            'admin_id': admin_id,
            'name': name,
            'role': role
        }

        # Insert the user data into MongoDB
        admins_collection.insert_one(user_data)

        # Generate a JWT token for the user
        access_token = create_access_token(identity=email)

        return {
            'access_token': access_token,
            'role': role
        }, 200

class AdminLoginResource(Resource):
    def post(self):
        data = user_login_parser.parse_args()
        email = data.get('email')
        password = data.get('password')

        # Retrieve the user document from MongoDB
        user_data = admins_collection.find_one({'email': email})

        if user_data and pbkdf2_sha256.verify(password, user_data['password']):
            # Password is correct, generate a JWT token
            access_token = create_access_token(identity=email)
            return {
                'access_token': access_token,
                'role': user_data["role"]
            }, 200
        else:
            return {'error': 'Invalid credentials'}, 401

class DetailsRegisterResource(Resource):
    @jwt_required()
    def post(self):
        data = details_parser.parse_args()
        student_id = data.get('student_id')
        department_id = data.get('department_id')
        company_name = data.get('company_name')
        package = data.get('package')
        year = data.get('year')

        # Check if the details already exists

        

        # Create the details document
        details_data = {
            'student_id': student_id,
            'department_id': department_id,
            'company_name': company_name,
            'package': package,
            'year': year
        }

        # Define the student_id of the document you want to update
        student_id_to_update = student_id

        # Define the new attribute name
        new_attribute_name = 'companies'

        # Define the company name and salary package to add

        # Check if the document already has the new attribute
        existing_student = students_collection.find_one({'student_id': student_id_to_update})

        if existing_student:
            # The document exists, check if the new attribute already exists
            if new_attribute_name not in existing_student:
                # If the new attribute doesn't exist, create it as a list with the current company
                new_attribute_value = [{'company_name': company_name, 'package': package}]
            else:
                # If the new attribute already exists, append the current company to the list
                existing_placement_history = existing_student[new_attribute_name]
                new_attribute_value = existing_placement_history + [{'company_name': company_name, 'package': package}]

            # Update the selected document to add or update the new attribute
            result = students_collection.update_one(
                {'student_id': student_id_to_update},
                {
                    '$set': {
                        new_attribute_name: new_attribute_value
                    }
                }
            )

                        # Create an EmailMessage object
            # msg = EmailMessage()

            # # Set the sender email address
            # msg.set_content(f"You are selected for {company_name} with {package}LPA")

            # # Set the recipient email address
            # msg['Subject'] = "Placement_Dept"
            # msg['From'] = "t@gmail.com"
            # msg['To'] = "@gmail.com"

            # # # Set up the SMTP server for Gmail
            # # smtp_server = "smtp.gmail.com"
            # # smtp_port = 587

            # # Log in to your Gmail account
            # # username = "@gmail.com"
            # # password = ""



            # try:
            #     server = smtplib.SMTP(smtp_server, smtp_port)
            #     server.starttls()
            #     server.login(username, password)
            # except Exception as e:
            #     print("Error: Unable to connect to the SMTP server.")
            #     print(e)
            

            
            # # try:
            # #     server = smtplib.SMTP(smtp_server, smtp_port)
            # #     server.starttls()
            # #     print(username, password)
            # #     server.login(username, password)
            # # except Exception as e:
            # #     print("Error: Unable to connect to the SMTP server.")
            # #     print(e)


            # msg_title = "Placement Connect"
            # sender = "smk123test@gmail.com"
            # msg = Message(msg_title,sender=sender,recipients=["saimanikumar67@gmail.com"])
            # msg_body = f"You are selected for {company_name} with {package}LPA"

            # try:
            #     mail.send(msg)
            # except Exception as e:
            #     print(e)
            #     # return f"the email was not sent {e}"







            # Check if the update was successful
            if result.modified_count > 0:
                print(f"Updated the '{new_attribute_name}' attribute for the document with student_id '{student_id_to_update}'.")
            else:
                print("No documents were updated.")
        else:
            print(f"Student with student_id '{student_id_to_update}' not found.")

        placements_collection.insert_one(details_data)

        return {
            'student_id': student_id
        }, 200
    
    @jwt_required()
    def get(self):
        all_details = placements_collection.find({})
        
        # Use json_util to serialize the MongoDB documents
        # details_list = {json_util.dumps(detail) for detail in all_details}
        
        # Return the list of students as JSON
        s = []
        for document in all_details:
            s.append({'student_id': document.get('student_id'), 'department_id': document.get('department_id'), 'company_name': document.get('company_name'), 'package': document.get('package'), 'year': document.get('year')})

        #     s.append(s1)
        # print(s)

        return s, 200

# class DetailsRegisterResource(Resource):
#     @jwt_required()
#     def post(self):
#         data = details_parser.parse_args()
#         student_id = data.get('student_id')
#         department_id = data.get('department_id')
#         company_name = data.get('company_name')
#         package = data.get('package')
#         year = data.get('year')

#         # Check if the details already exists
        

#         # Create the details document
#         details_data = {
#             'student_id': student_id,
#             'department_id': department_id,
#             'company_name': company_name,
#             'package': package,
#             'year': year
#         }

#         # Insert the user data into MongoDB
#         student_id_to_update = student_id

#         # Define the company name to add
#         company_name_to_add = 'company_name'

#         # Check if the student document with the provided student_id exists
#         student_doc = students_collection.find_one({'student_id': student_id_to_update})

#         if student_doc:
#             # Check if the 'companies' attribute exists in the document
#             if 'companies' in student_doc:
#                 # Append the new company name to the existing list
#                 result = students_collection.update_one(
#                     {'student_id': student_id_to_update},
#                     {'$push': {'companies': company_name_to_add}}
#                 )
#             else:
#                 # Create the 'companies' attribute with a list containing the initial company name
#                 result = students_collection.update_one(
#                     {'student_id': student_id_to_update},
#                     {'$set': {'companies': [company_name_to_add]}}
#                 )

#             # Check if the update was successful
#             if result.modified_count > 0:
#                 print(f"Added '{company_name_to_add}' to the list of companies for student with student_id '{student_id_to_update}'.")
#             else:
#                 print("No documents were updated.")
#         else:
#             print(f"Student with student_id '{student_id_to_update}' not found.")
        
#         # Insert the user data into MongoDB
#         placements_collection.insert_one(details_data)

#         return {
#             'student_id': student_id
#         }, 200
    
#     @jwt_required()
#     def get(self):
#         all_details = placements_collection.find({})
        
#         # Use json_util to serialize the MongoDB documents
#         # details_list = {json_util.dumps(detail) for detail in all_details}
        
#         # Return the list of students as JSON
#         s = []
#         for document in all_details:
#             s.append({'student_id': document.get('student_id'), 'department_id': document.get('department_id'), 'company_name': document.get('company_name'), 'package': document.get('package'), 'year': document.get('year')})

#         #     s.append(s1)
#         # print(s)

    

#         return s, 200

class StudentsData(Resource):
    @jwt_required()
    def get(self, id):

        # Find the student document by student_id
        # args = st_parser.parse_args()
        # student_id = args.get('id')
        student_id = str(id)
        print(student_id)
        
        student_data = students_collection.find_one({'student_id': student_id})
        
        if student_data:
            # Check if the attribute containing a list of JSONs exists in the student document
            if 'companies' in student_data:
                print(student_data['companies'])
                # Return the list of JSONs for the specified attribute
                attribute_data = student_data['companies']
                return attribute_data, 200
            else:
                attribute_data = []
                return attribute_data, 200
                # return {'error': 'Attribute not found for the specified student.'}, 404
        else:
            return {'error': 'Student not found.'}, 404
        
class DepartmentDetails(Resource):
    @jwt_required()
    def get(self, id):
        # Fetch all documents with the given department_id from "placement_details" collection
        department_details = list(placements_collection.find({'department_id': str(id)}))
        print(department_details)
        s = []
        for document in department_details:
            s.append({'student_id': document.get('student_id'), 'department_id': document.get('department_id'), 'company_name': document.get('company_name'), 'package': document.get('package'), 'year': document.get('year')})

        #     s.append(s1)
        # print(s)
        return s, 200
        # Return the department details as JSON
        # return jsonify(department_details)


class UploadJpg(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=str, required=True, help='Student ID is required')
        parser.add_argument('company', type=str, required=True, help='Company name is required')
        parser.add_argument('dept_id', type=str, required=True, help='Department ID is required')
        parser.add_argument('image', type=werkzeug.datastructures.FileStorage, location='files', required=True, help='Image file is required')

        args = parser.parse_args()

        student_id = args['student_id']
        company = args['company']
        dept_id = args['dept_id']

        image_file = args['image']

        # Convert the image to bytes
        image_bytes = io.BytesIO()
        image = Image.open(image_file)
        image.save(image_bytes, format='JPEG')

        image_data = {
            'student_id': student_id,
            'company': company,
            'dept_id': dept_id,
            'data': image_bytes.getvalue()
        }

        # Insert the image data into MongoDB
        image_id = images.insert_one(image_data).inserted_id

        return {'message': 'Image uploaded successfully', '_id': str(image_id)}, 201

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('student_id', type=str, required=True, help='Student ID is required')
        parser.add_argument('company', type=str, required=True, help='Company name is required')
        parser.add_argument('dept_id', type=str, required=True, help='Department ID is required')

        args = parser.parse_args()

        student_id = args['student_id']
        company = args['company']
        dept_id = args['dept_id']

        # Find the image data in MongoDB based on student_id, company, and dept_id
        image_data = images.find_one({'student_id': student_id, 'company': company, 'dept_id': dept_id})

        if image_data:
            image_bytes = image_data['data']
            image = Image.open(io.BytesIO(image_bytes))
            return image

        return {'message': 'Image not found'}, 404



api.add_resource(UploadJpg,'/api/jpg_handler')

api.add_resource(DepartmentDetails,'/api/dept_details/<int:id>')  
api.add_resource(StudentsData,'/api/student_details/<int:id>')
api.add_resource(StudentRegisterResource, '/api/stu_register')
api.add_resource(StudentLoginResource, '/api/stu_login')

api.add_resource(DepartmentRegisterResource, '/api/dept_register')
api.add_resource(DepartmentLoginResource, '/api/dept_login')

api.add_resource(AdminRegisterResource, '/api/admin_register')
api.add_resource(AdminLoginResource, '/api/admin_login')

api.add_resource(DetailsRegisterResource,'/api/details_register')


if __name__ == '__main__':
    app.run(debug=True, port=8080)