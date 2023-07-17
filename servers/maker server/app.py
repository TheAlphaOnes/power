from flask import Flask,request,jsonify
from flask_cors import CORS

from app_manager import *
app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "<--- power dev server --->"

@app.route("/alldata")
def all_data():
    
    return jsonify(full_data())

@app.route("/login",methods=['GET','POST'])
def login():
    data = request.json
    user =  data.get("username")
    passw = data.get("password")
    reply = check_login(username=user,passw=passw)
    return jsonify({"status":reply})

if __name__ == "__main__":
    app.run(debug=True)