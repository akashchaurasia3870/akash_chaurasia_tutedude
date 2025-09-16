from flask import Flask,jsonify,request
from pymongo import MongoClient
import json
import os 
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

MONGODBURL = os.getenv('MONGODBURL')
client = MongoClient(MONGODBURL)
db = client['flaskdb']

@app.route('/api',methods=["GET"])
def get_data():
    with open('data.json','r') as file:
        data = json.load(file)
    return jsonify(data)

@app.route('/submit',methods=["POST"])
def submit_data():
    try:
        name = request.form['name']
        age = request.form['age']
        collection = db['users']
        collection.insert_one({'name':name,'age':age})
        return jsonify({"status": True})
    except Exception as e:
        print(str(e))
        return jsonify({"status": False})

@app.route('/submittodoitem',method=["POST"])  
def submit_todo_item():
    try:
        name = request.form['itemName']
        desc = request.form['itemDescription']
        collection = db['items']
        collection.insert_one({'itemName':name,'itemDescription':desc})
        return jsonify({'status':True})
    except Exception as e:
        print(str(e))
        return jsonify({'status':False}) 


if __name__=='__main__':
    app.run(host="0.0.0.0", port=3000,debug=True)



