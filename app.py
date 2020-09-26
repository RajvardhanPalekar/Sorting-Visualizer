from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from random import randint
import json

from utils import sort_util

app = Flask(__name__)
app.secret_key = "session_secret"


@app.route("/")
def home():
    array_object = {
        "array" : [],
        "sorted_array": [],
        "iter_loc": 0,
        "current" : 0,
        "swap": None,
        "sorted": False
    }
    array_object['array'] = [ randint(50, 500) for x in range(30) ]
    session["array_object"] = array_object
    return render_template("sort.html" , array = array_object['array'])

@app.route("/sort", methods = ["POST"])
def sort_list():
    try:
        if "array_object" in session:
            sortType = request.form['sortType']
            array_object = sort_util.sort_one(session['array_object'], sortType)
            session["array_object"] = array_object
            return jsonify({"array_object": array_object})
        else:
            return redirect(url_for("/"))
        
    except Exception as ex:
        print(ex)
        return jsonify({"error" : str(ex)})


if __name__ == "__main__":
    app.run(debug=True)