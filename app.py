from flask import Flask, render_template, request, redirect, make_response

# Configure app
app = Flask(__name__)

# Configure session and cookie
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Global name
name = ""

# Dictionary to store names:items{}
names = {}

# Dictionary to store items
items = {}

# Routes
@app.route("/")
def index():
    # Get name from session cookie
    name = request.cookies.get("name")
    # Force login
    if name == "" or name == None:
        return redirect("/login")
    # Load existing items or create new items{}
    if not name in names:
        names[name] = {}
    return render_template("index.html", items=names[name], name=name)

@app.route("/login")
def login():
    global name
    # Check if name gets passed
    name = request.args.get("name", "")
    if not name:
        return render_template("login.html")
    else:
        res = make_response(redirect("/"))
        res.set_cookie("name", name)
        return res

@app.route("/logout")
def logout():
    global name
    name = ""
    res = make_response(redirect("/login"))
    res.delete_cookie("name")
    return res

@app.route("/update")
def update():
    # Get name from session cookie
    name = request.cookies.get("name")
    # Force login
    if name == "" or name == None:
        return redirect("/login")
    if name == "" or name == None:
        return "Please <a href='/login'>log in</a>"
    return render_template("update.html", items=names[name], name=name)

@app.route("/add")
def add():
    # Get name from session cookie
    name = request.cookies.get("name")
    # Force login
    if name == "" or name == None:
        return redirect("/login")
    item = request.args.get("item", "default")
    if item in names[name]:
        names[name][item] += 1
    else:
        names[name][item] = 1
    print(f"added: {item}")
    return redirect("/")

@app.route("/remove")
def remove():
    # Get name from session cookie
    name = request.cookies.get("name")
    # Force login
    if name == "" or name == None:
        return redirect("/login")
    item = request.args.get("item", "default")
    if item in names[name]:
        del names[name][item]
    print(f"removed: {item}")
    return redirect("/")