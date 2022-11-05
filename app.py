import sqlite3
from flask import Flask, request, render_template, redirect, session
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager
from flask_session import Session


# flask init
app = Flask(__name__)
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


# flask login
flask_login = LoginManager()


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/user_cabinet', methods=['GET', 'POST'])
def profile():
    return render_template('user_cabinet.html')


if __name__ == "__main__":
    app.run(debug=True)



# {% extends "layout.html" %}

# {% block body %}

#     {% if session.name %}
#         You are logged in as {{ session.name }}. <a href="/logout">Log out</a>.
#     {% else %}
#         You are not logged in. <a href="/login">Log in</a>.
#     {% endif %}

# {% endblock %}


# {% for zxc in goods_left%}

# <p>LEFT {{zxc[0]}}</p>
# <p>STILL {{zxc[1]}}</p>
# <p>YOURS {{zxc[2]}}</p>

# {% endfor %}
