from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient
client = MongoClient('')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('main.html')

@app.route('/addcard')
def addcard():
   return render_template('addcard.html')

@app.route("/movie-list", methods=["POST"])
def movie_save():
    movie_list = list(db.movies.find({}, {'_id': False}))
    if len(movie_list) == 0:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        data = requests.get('https://movie.naver.com/movie/running/current.naver', headers=headers)

        soup = BeautifulSoup(data.text, 'html.parser')

        ul = soup.find('ul', class_='lst_detail_t1')
        img = ul.select('li > div > a > img')

        count = 0

        for i in img:
            count = count + 1
            movie = {
                'num': count,
                'movie_name': i.get('alt'),
                'movie_img': i.get('src')
            }
            db.movies.insert_one(movie)

    movie_list = list(db.movies.find({}, {'_id': False}))
    return jsonify({'movies': movie_list})

@app.route("/movie-list", methods=["GET"])
def movie_get():
    movie = db.movies.find_one({'num': int(request.args.get('id'))}, {'_id': False})
    return jsonify({'movies': movie})

@app.route("/add-card", methods=["POST"])
def card_post():
    movie_name_receive = request.form['movie_name_give']
    movie_img_receive = request.form['movie_img_give']
    date_receive = request.form['date_give']
    star_receive = request.form['star_give']
    comment_receive = request.form['comment_give']

    card = {
        'movie_name': movie_name_receive,
        'movie_img': movie_img_receive,
        'date': date_receive,
        'star': star_receive,
        'comment': comment_receive
    }

    db.cards.insert_one(card)
    return jsonify({'result': 'ok'})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)