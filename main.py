from flask import Flask, request,render_template
from fun import *

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        registration(request.form["username"],request.form["age"],request.form["address"],request.form["course"],request.form["duration"])
        
    return render_template("stud_mang.html")

if __name__=="__main__":
    app.run(debug=True)