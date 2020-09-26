from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from random import randint
import json

app = Flask(__name__)
app.secret_key = "session_secret"
array = []

# array_object = {
#     "array" : [],
#     "sorted_array": [],
#     "current" : [0],
#     "swapped": [0],
#     "sorted": False
# }

@app.route("/")
def home():
    array = [ randint(50, 500) for x in range(50) ]
    session["array"] = array
    return render_template("sort.html" , array = array)

@app.route("/sort", methods = ["POST"])
def sort_list():
    try:
        if "array" in session:
            array = session["array"]

            array.sort()
            # Sorting method here
            return jsonify({"array" : array, "sorted": True})
        else:
            return redirect(url_for("/"))
        
    except Exception as ex:
        print(ex)
        return jsonify({"error" : str(ex)})


if __name__ == "__main__":
    app.run(debug=True)