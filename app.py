import jwt
import datetime
import hashlib
from flask import Flask, render_template, jsonify, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime, timedelta


app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
app.config['UPLOAD_FOLDER'] = "./static/profile_pics"

SECRET_KEY = 'SPARTA'

from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.ub1o9.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/sign-up')
def signup():
    return render_template('sign-up.html')

@app.route('/my-card')
def mycard():
    return render_template('mycard.html')

# ----- sign-up ----- #

@app.route('/')
def home():
    token_receive = request.cookies.get('mytoken')
    try:
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])

        return render_template('index.html')
    except jwt.ExpiredSignatureError:
        return redirect(url_for("login", msg="로그인 시간이 만료되었습니다."))
    except jwt.exceptions.DecodeError:
        return redirect(url_for("login", msg="로그인 정보가 존재하지 않습니다."))

@app.route('/sign_up/save', methods=['POST'])
def sign_up():
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']
    password_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
    doc = {
        "username": username_receive,
        "password": password_hash,
    }
    db.users.insert_one(doc)
    return jsonify({'result': 'success'})


@app.route('/sign_up/check_dup', methods=['POST'])
def check_dup():
    username_receive = request.form['username_give']
    exists = bool(db.users.find_one({"username": username_receive}))
    return jsonify({'result': 'success', 'exists': exists})

# ----- sign-up ----- #

# ----- my-page ----- #

@app.route("/mycard", methods=["GET"])
def mycard_get():
    cards_list = list(db.cards.find({}, {'_id': False}))
    return jsonify({'cards':cards_list})



if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)