from flask import Flask,jsonify,render_template,request,redirect,url_for
import requests
import os 
from dotenv import load_dotenv

load_dotenv()
SERVER_URL = os.getenv("SERVER_URL")

app = Flask(__name__)

@app.route('/api',methods=["GET"])
def get_data():
    try:
        response = requests.get(f'{SERVER_URL}/api')
        response.raise_for_status()
        return jsonify(response.json())
    except Exception as e:
        return jsonify({"error":str(e)}),500

@app.route('/submit',methods=["GET"])
def get_submit_page():
        return render_template('form.html')

@app.route('/submit',methods=["POST"])
def submit_data():
    try:
        response = requests.post(f'{SERVER_URL}/submit',request.form)
        response.raise_for_status()
        if(response.json()['status']):
            return redirect(url_for('success_page'))
        else:
            return render_template('form.html',error=str(e))
    except Exception as e:
            return render_template('form.html',error=str(e))

    
@app.route('/success')
def success_page():
    return render_template("success.html")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000,debug=True)



