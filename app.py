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
    return render_template('index.html', title='Welcome to Arcadia')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/offerings')
def offerings():
    return render_template('offerings.html', title='Offerings')

@app.route('/community')
def community():
    return render_template('community.html', title='Community')

@app.route('/register')
def register():
    return render_template('register.html', title='Join the community')


@app.route('/subscribe')
def subscribe():
    pass


if __name__ == '__main__':
    app.run(debug=True)