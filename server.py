from flask import Flask
from pymongo import MongoClient
from flask import request, jsonify, render_template
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

murl = "mongodb://localhost:27017/"
client = MongoClient(murl)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/signup', methods = ["POST"])
def signup():
    internship = client["internship"]
    student = internship["student"]
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    password = request.form.get('password', '')
    # Ideally should hash and store password but meh
    student.insert({"name": name, "email": email, "password": password})
    return 'Done'

@app.route('/login')
def login():
    pass


@app.route('/students')
def listStudents():
    internship = client["internship"]
    student = internship["student"]
    for s in student.find({}):
        print(s)
    return jsonify(list(student.find({})))    


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5500)