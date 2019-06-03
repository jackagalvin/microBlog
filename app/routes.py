from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {"username":"jack"}
    posts = [
        {
            "author" : {"username" : "John"},
            "body" : "Jet fuel can't melt steel beams"
        },
        {
            "author" : {"username" : "Sally"},
            "body" : "Yes it can"
        }
    ]
    return render_template("index.html",title="Home",user=user,posts=posts)
