from flask import Flask, url_for, render_template
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

load_dotenv('.env')

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
csrf_token = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    pass

@app.route('/offerings')
def offerings():
    pass

@app.route('/community')
def community():
    pass

@app.route('/subscribe')
def subscribe():
    pass


if __name__ == '__main__':
    app.run(debug=True)