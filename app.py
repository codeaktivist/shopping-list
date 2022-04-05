from flask import Flask, render_template, request, redirect

app = Flask(__name__)

items = {}

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/add")
def add():
    item = request.args.get("item", "default")
    if item in items:
        items[item] += 1
    else:
        items[item] = 1
    print(f"added: {item}")
    return redirect("/")
    # return render_template("add.html", item=item, items=items)

@app.route("/remove")
def remove():
    item = request.args.get("item", "default")
    if item in items:
        del items[item]
    print(f"removed: {item}")
    return redirect("/")
    # return render_template("remove.html", item=item, items=items)

