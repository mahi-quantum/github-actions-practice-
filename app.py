# this code is from other repo 
# flask app
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')
    return None 

if none:
    go


@app.route('/health')
def health():
    return 'Server is up and running'
