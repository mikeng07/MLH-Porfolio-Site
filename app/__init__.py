import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Leanring", url=os.getenv("URL"))
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')