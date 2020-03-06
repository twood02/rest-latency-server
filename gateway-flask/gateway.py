## TO INSTALL FLASK
 ## Optional: setup a virtual environment
 # python3 -m venv venv
 # . venv/bin/activate
 ## Install Flask and the requests package
 # pip install Flask
 # pip install requests
### TO RUN FLASK
 # export FLASK_APP=gateway.py
 # flask run


from flask import Flask
app = Flask(__name__)

import requests

@app.route('/')
def hello_world():
    req = requests.get("http://localhost:8080/request")
    return 'Hello, World! Response was: ' \
    	+ str(req.text)
