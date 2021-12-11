from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, ValidationError


app=Flask(__name__)
db= SQLAlchemy(app)
app.config['SQLACHEMY_DATABASE_URI']= 'sqlite://database.db'
app.config['SECRET_KEY']= 'swertekapagnahulaanmo'

class User(db.Model, UserMixin):
      id = db.Column(db.Integer, primary_key=True)
      username = db.Column(db.String(20), primary_key=True, unique=True)
      password = db.Column(db.String(80), primary_key=True)

class RegisterForm(FlaskForm):
      username= StringField(validators=[InputRequired(),Length(min=4, max=20)], render_kw={"placeholder": "Username"})
      passwod= StringField(validators=[InputRequired(),Length(min=4, max=20)], render_kw={"placeholder": "Password"})
      submit =SubmitField ("Register")

      def validate_username(self,username):
            existing_user_username = User.query.filter_by(username=username.data).first()

            if existing_user_username:
                  raise ValidationError("Username Already exists! Please Try Again.")

class LoginForm(FlaskForm):
      username= StringField(validators=[InputRequired(),Length(min=4, max=20)], render_kw={"placeholder": "Username"})
      passwod= StringField(validators=[InputRequired(),Length(min=4, max=20)], render_kw={"placeholder": "Password"})
      submit =SubmitField ("Login")

@app.route('/')
def index():
  return render_template('try-index.html')

@app.route('/login', method=['GET','POST'])
def login():
  return render_template('login.html')

@app.route('/register', method=['GET','POST'])
def register():
  return render_template('register.html')

if __name__ == '__main__':
  app.run(debug=True)