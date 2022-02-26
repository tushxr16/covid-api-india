from flask import Flask, jsonify, render_template, request
from crud import getJsonofState

app = Flask(__name__)

list_of_available_states = ["India", "Bihar", "Chandigarh", "Delhi"]


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        a = request.form["state"]
        return str(a)
    else:
        return render_template("index.html", states=list_of_available_states)


@app.route("/api/<string:state>")
def appi(state):
    ret = getJsonofState(state)
    return jsonify(ret)


@app.route("/about")
def about():
    return "About Us"


@app.route("/api-json")
def api():
    return app.send_static_file("dt.json")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
