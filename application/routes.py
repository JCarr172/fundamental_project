from application import app, db
#from application.models import Army
from flask import render_template, request, redirect, url_for
#from application.forms import ArmyForm


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title = 'Home')
