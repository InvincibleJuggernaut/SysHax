from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from passlib.hash import pbkdf2_sha256
import os

from test_evaluation import *
from compression import *
from location import *
from wipers import *

UPLOAD_FOLDER='/home/devops/Development/Hackathons/Gov-TechThon/Uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
ALLOWED_VIDEO_EXTENSIONS={'mp4'}

app=Flask(__name__)

app.config['UPLOAD_FOLDER']= UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RTO Credentials'
app.config['SECRET_KEY']='secret'
app.config['SQLALCHEMY_BINDS'] = {
    'db': 'sqlite:///RTO Credentials'
}
db=SQLAlchemy(app)

login_manager=LoginManager()
login_manager.init_app(app)

location=get_location()
result.append(location)

class Officer(db.Model, UserMixin):
    __bind_key__='db'
    __tablename__="RTO Officer details"
    id=db.Column(db.Integer, primary_key=True, autoincrement=True)
    name=db.Column(db.String(100), nullable=False)
    email=db.Column(db.String(100), nullable=False)
    password=db.Column(db.String(500), nullable=False)

    def __init__(self, name, email, password):
        self.name=name
        self.email=email
        self.password=password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

@login_manager.user_loader
def load_user(user_id):
    return Officer.query.get(int(user_id))

@app.route('/')
def home():
    return render_template('home.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def allowed_video(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_VIDEO_EXTENSIONS

@app.route('/testing', methods=['GET', 'POST'])
@login_required
def upload_file():
    counter = 1
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            return redirect(request.url)
        if file and allowed_file(file.filename):
            #location=get_location()
            filename = secure_filename(file.filename)
            file_location =os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_location)
            if(counter==1):
                result=predict_damage(file_location)
            elif(counter==2):
                result=predict_windscreen(file_location)
            elif(counter==3):
                result=predict_side_mirror(file_location)
            counter+=1
            message="Files uploaded successfully"
            return render_template('testing.html', message=message)
        elif file and allowed_video(file.filename):
            filename = secure_filename(file.filename)
            file_location = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            result = wiper(file_location)
            file.save(file_location)
    elif request.method =='GET':
        return render_template('testing.html')
    else:
        return render_template('result.html', message="Please sign-in")


@app.route('/testing')
def result_form():
    try:
        option1 = request.form.getlist('one')
        option2 = request.form.getlist('two')
        return render_template('report.html', option1=option1, option2=option2)
    except:
        return render_template('report.html')


@app.route('/signup')
def signup_load():
    return render_template('signup.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method=='POST':
        officer_name=request.form['name']
        officer_email=request.form['email']
        officer_pass=request.form['password']
        check=Officer.query.filter_by(email=officer_email).first()
        if check is not None:
            return render_template('signup.html', message='This email already exists')
        else:
            officer_pass=pbkdf2_sha256.hash(officer_pass)
            collected_data=Officer(officer_name, officer_email, officer_pass)
            db.session.add(collected_data)
            db.session.commit()
            message="You have successfully signed up"
            return render_template('result.html', message=message)
    else:
        message='Sign up failed. Try again'
        return render_template('result.html', message=message)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method=='POST':
        officer_email=request.form['email']
        officer_pass=request.form['password']
        check=Officer.query.filter_by(email=officer_email).first()
        if check is None:
            return render_template('signin.html', message="The account doesn't exist.")
        elif(pbkdf2_sha256.verify(officer_pass, check.password)==True):
            login_user(check)
            return render_template('user.html', name=check.name, email=check.email)
        else:
            return render_template('signin.html', message='The account credentials are wrong')
    else:
        return render_template('signin.html')

@app.route('/signout')
@login_required
def signout():
    logout_user()
    return render_template('result.html', message="You are logged out")

@app.route('/user')
@login_required
def user():
    return render_template('user.html')

@app.route('/report')
@login_required
def report():
    result=generate_result()
    return render_template('report.html', result1=result[0], result2=result[1], result3=result[2])

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)
