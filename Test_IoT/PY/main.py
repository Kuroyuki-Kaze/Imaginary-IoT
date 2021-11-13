from flask.helpers import make_response
from flask import Flask, request, redirect
from flask_cors import CORS
from os import path


app = Flask(__name__)
CORS(app)


state_on = False

p = path.abspath('Imaginary Iot\\Test_IoT\\HTML\\template.html')

with open(p, 'r') as f:
    template_form = f.read()

@app.route('/')
def red_home():
    return redirect('/home/')


@app.route('/home/', methods=['GET'])
def home():
    global state_on

    status = "On" if state_on else "Off"

    return status

@app.route('/submit/', methods=['POST', 'OPTIONS'])
def change_status():
    global state_on

    if request.method == "POST":
        json_data = request.json
        temp_action = json_data['action'] if json_data else "no"
        if temp_action == "on":
            state_on = True
            return "200 OK"
        elif temp_action == "off":
            state_on = False
            return "200 OK"
        else:
            return "406 Not Acceptable"

    elif request.method == "OPTIONS":
        resp = make_response()

        # THIS IS VERY DANGEROUS, SHOULD NOT ALLOW ANYONE TO CONTROL THE IOT
        resp.headers.add("Access-Control-Allow-Origin", "*")

        resp.headers.add("Access-Control-Allow-Headers", "*")
        resp.headers.add("Access-Control-Allow-Methods", "*")
        return resp

if __name__ == "__main__":
    app.run()