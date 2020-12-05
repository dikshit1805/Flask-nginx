import os
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, DecimalField, TextAreaField, validators
from wtforms.validators import DataRequired
from wtforms.fields.html5 import DateField

app = Flask(__name__)
bootstrap = Bootstrap(app)

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
        result = requests.get(url="http://127.0.0.1:5000/searchUser?name='"+form.userID.data+"'")
        return render_template('index.html', result=result, form=form)
    return render_template('index.html',result=None, form=form)

@app.route('/AddUser', methods=['GET', 'POST'])
def AddUser():
    form = AddUserForm()
    if request.method == 'POST':
        params = {"userID":form.userID.data,"key":form.key.data}
        result = requests.post(url="http://127.0.0.1:5000/addUser", data=params)
        return render_template('AddUser.html', result=result, form=form)
    return render_template('AddUser.html',result=None, form=form)

if __name__ == '__main__':
    port = int(os.getenv('PORT', '6000'))
    app.run(host='127.0.0.1',port=port)