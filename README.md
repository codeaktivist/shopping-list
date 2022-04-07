# flask-shopping-list
A simple shopping list web app to play around with the Flask microframework.

*v 1.0.0 DBLess*

## Installation

install python3:

https://www.python.org/downloads/

Optional: Setup a virtual environment for python to run in:

`$ python3 -m venv venv`

install Flask:

`$ pip install -U Flask`

run flask on localhost:

`$ flask run`

or expose to outside world:

`$ flask run --host=0.0.0.0`

Optional: Run flask in developer mode to see debug information

`$ export FLASK_ENV=development`

The interface is now accessible via port 5000
http://localhost:5000/


## Usage

Enter your name to continue your shopping list. New users will start with an empty list.
Check off items when done shopping. Easy :)

## Under the hood

This version is **DBless** just for the fun of it. Items and Users are NOT persistent and only live in RAM.