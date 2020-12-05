import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, DecimalField, TextAreaField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField
from flask_bootstrap import Bootstrap
import requests
from flask_cors import CORS

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'blah blah blah blah'
CORS(app)

class SearchUser(FlaskForm):
    userID = StringField('User ID ', validators=[DataRequired()], default=None)
    submit = SubmitField('Search')

class AddUserForm(FlaskForm):
    userID = StringField('User ID ', validators=[DataRequired()], default=None)
    key = StringField('Secret Key ', validators=[DataRequired()], default=None)
    submit = SubmitField('ADD User')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = SearchUser()
    if request.method == 'POST':
        result = requests.get(url="http://nginx:80/rest/searchUser?name={}".format(form.userID.data))
        return render_template('index.html', result=result.json(), post=1, form=form)
    return render_template('index.html',result=None, post=0, form=form)

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUser():
    form = AddUserForm()
    if request.method == 'POST':
        params = {"userID":form.userID.data,"key":form.key.data}
        result = requests.post(url="http://nginx:80/rest/addUser", data=params)
        return render_template('AddUser.html', result=result.json(), post=1,  form=form)
    return render_template('AddUser.html',result=None, post=0, form=form)

@app.route('/GetAllUsers', methods=['GET'])
def GetAllUsers():
    result = requests.get(url="http://nginx:80/rest/getAllUsers")
    return render_template('GetAllUser.html', result=result.json())

if __name__ == '__main__':
    app.run(debug=True)
