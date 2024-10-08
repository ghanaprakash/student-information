from flask import Flask, request,render_template,redirect
from fun import *

app=Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():
    if request.method=="POST":
        registration(request.form["username"],request.form["age"],request.form["address"],request.form["course"],request.form["duration"])
    data=json_read()
    return render_template("stud_mang.html",student=data["student"])

@app.route("/delete/<id>")
def delete_stud(id):
     delete(id)
     return redirect("/")
 
@app.route("/update/<id>" ,methods=["GET","POST"])
def update_stud(id):
     update(id,request.form["username"],request.form["age"],request.form["address"],request.form["course"],request.form["duration"])
     return redirect("/")

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0")