from flask import Flask, redirect, make_response, render_template, request, session
import sqlite3

# Configure app
app = Flask(__name__)
app.secret_key = "dontyoustoreyoursuperdupersecretkeyhere"

# Database schema for reference
# CREATE TABLE Users (UserID INTEGER PRIMARY KEY, Name varchar(20) NOT NULL UNIQUE);
# CREATE TABLE Lists (ListID INTEGER PRIMARY KEY, UserID INTEGER, Item varchar(20) NOT NULL, Count INTEGER, FOREIGN KEY(UserID) REFERENCES Users(UserID));

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
    
    # Get items of user from db
    con = sqlite3.connect("shopping.db")
    cur = con.cursor()
    item_list = cur.execute("SELECT Item FROM Lists WHERE UserID = ?", [session["UserID"]]).fetchall()
    print(item_list)
    con.close()


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
    # add user to db if not allready existing
    con = sqlite3.connect("shopping.db")
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO Users (Name) VALUES (:name)", {"name": name})
    session["UserID"] = cur.execute("SELECT UserID FROM Users WHERE Name = :name", [name]).fetchone()[0]
    con.commit()
    con.close()
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

    # Get items of user from db
    con = sqlite3.connect("shopping.db")
    cur = con.cursor()
    cur.execute("INSERT INTO Lists (UserID, Item, Count) VALUES (:UserID, :Item, :Count)", {"UserID": session["UserID"], "Item": item, "Count": 0})
    con.commit()
    con.close()

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