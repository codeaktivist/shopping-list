from flask import Flask, redirect, make_response, render_template, request, session

# Configure app
app = Flask(__name__)
app.secret_key = "dontyoustoreyoursuperdupersecretkeyhere"

# Dictionary to store names:items{}
names = {}

# Dictionary to store items
items = {}

# Routes
@app.route("/")
def index():
    # Check active session
    if not "name" in session:
        return redirect("/login")
    # Read name from session
    name = session["name"]
    # Reject old session
    if not session["name"] in names:
        return redirect("/logout")

    return render_template("index.html", items=names[name], name=name)

@app.route("/login", methods=["GET", "POST"])
def login():
    # GET: present login form to user
    if request.method == "GET":
        return render_template("login.html")
    # POST: user submitted login form
    name = request.form.get("name")
    # no name -> redirect to login
    if not name:
        return redirect("/login")
    # check name -> redirect to login
    if len(name) == 0 or len(name) > 20:
        return redirect("/login")
    # new name -> add empty items dictionary
    if not name in names:
        names[name] = {}
    # set session name
    session["name"] = name
    return redirect("/")

@app.route("/logout")
def logout():
    # delete session name
    session.pop("name", None)    
    return redirect("/login")

@app.route("/update")
def update():
    # Check active session
    if not "name" in session:
        return "<p>Error, please <a href='/login'>log in</a>!</p>"
    # Read name from session
    name = session["name"]
    # Reject old session
    if not session["name"] in names:
        return "<p>Error, please <a href='/login'>log in</a>!</p>"

    # Respond updated items
    return render_template("update.html", items=names[name], name=name)

@app.route("/add", methods=["GET"])
def add():
    # Check active session
    if not "name" in session:
        return redirect("/login")
    # Read name from session
    name = session["name"]
    # Reject old session
    if not session["name"] in names:
        return redirect("/logout")

    # Get item, add item
    item = request.args.get("item")
    if item in names[name]:
        names[name][item] += 1
    else:
        names[name][item] = 1
    return render_template("update.html", items=names[name], name=name)

@app.route("/remove", methods=["GET"])
def remove():
    # Check active session
    if not "name" in session:
        return redirect("/login")
    # Read name from session
    name = session["name"]
    # Reject old session
    if not session["name"] in names:
        return redirect("/logout")

    # Get item, remove item
    item = request.args.get("item")
    if item in names[name]:
        del names[name][item]
    return render_template("update.html", items=names[name], name=name)

def checkName():
    # Check active session
    if not "name" in session:
        return redirect("/login")
    # Read name from session
    name = session["name"]
    # Reject old session
    if not session["name"] in names:
        return redirect("/logout")