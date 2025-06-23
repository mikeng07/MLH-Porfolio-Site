import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    experiences = [
        {'title': 'Teaching Assistant', 'company' : 'CSULB'},
        {'title': 'Teaching Assistant', 'company' : 'El Camino'},

    ]

    educations = [
        {'degree' : 'AS', 'school' : 'El Camino College'},
        {'degree' : 'BS', 'school' : 'Cal Poly Pomona'},
        {'degree' : 'MS', 'school' : 'CalState Long Beach'}
    ]
    return render_template('index.html', title="Learning", url=os.getenv("URL"), experiences = experiences, educations = educations)
    


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')

