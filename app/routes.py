from flask import render_template
from app import app
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def index():
    user = {"username":"Jack"}
    posts = [
        {"author":{"username":"John"},
        "message":"Man it's cold today"},
        {"author":{"username":"Mark"},
        "message":"Can we be done with this weather please"}
    ]
    return render_template("index.html",title="Home",user=user,posts=posts)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html",title="Sign In",form=form)