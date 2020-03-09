#!flask/bin/python


from flask import Flask
import requests
from flask import request
import json

app = Flask(__name__)

def html(content):  # Also allows you to set your own <head></head> etc
   return '<html><body>' + content + '</body></html>'

@app.route('/')
def singleReq():
    req = requests.get("http://localhost:8080/request")

    resTime = req.json()
    
    return html('I RESTed for ' + str(resTime["data"]) + ' time units.' + '\n')

@app.route('/someEndPoint', methods = ['POST'])
def nRequest():
    reqData = request.get_json(force=True)
    nValue = reqData["numRequests"]

    totalTime = 0

    for i in range(nValue):
        req = requests.get("http://localhost:8080/request")
        resData = req.json()

        totalTime += resData["data"]
    

    return html('I made ' + str(nValue) + ' requests and it took ' + str(totalTime) + ' milliseconds.' + '\n') 


    



if __name__ == '__main__':
    app.run(debug=True)