from flask import Flask, render_template, request, jsonify,session, make_response
import jwt
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
from pymongo import MongoClient
from db import client
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import requests
import uuid
from functools import wraps
app = Flask(__name__)

app.config['SECRET_KEY'] = 'password'
def token_required(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        token = request.args.get('token')
        if not token:
            return jsonify({'alert':'Token is missing'})
        try:
            payload = jwt.decode(token, app.config['SECRET_KEY'])
        except:
            return jsonify({'alert':'Invalid Token'})
    return decorated


@app.route('/')
def login():
    if not session.get('logged in'):
        return render_template('login.html')
    else:
        return "logged in!"


@app.route('/public')
def public():
    return 'for public'


@app.route('/auth')
@token_required
def auth():
    return 'JWT verified'


@app.route('/login', methods = ["POST"])
def logged_in():
    if request.form['username'] and request.form['password'] == '1234':
        session['logged_in'] = True
        token = jwt.encode({
            'user': request.form['username'],
            'expiration': str(datetime.utcnow() + timedelta(seconds = 120))
        },
        app.config['SECRET_KEY'])
        return jsonify({'token':jwt.decode(token, algorithms=['HS256'])})
    else:
        return make_response('unable to verify', 403,
                             {'WWW-Authenticate':'Basic realm: "Authentication Failed'})






# def token_require(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = jwt.encode(
#                 payload=payload_data,
#                 key=my_secret
#                 )
#         if not token:
#             return jsonify({'msg':'token missing'}), 401
#         try:
#             data = jwt.decode(token, )
#         except:
#             return jsonify({'msg':'token invalid'}), 401
#         return f(*args, **kwargs)
#
#     return decorated
#
#
# @app.route('/unprotected')
# def unprotected():
#     return jsonify({'msg':'anyone can view this'})
#
#
# @app.route('/protected')
# @token_require
# def protected():
#     return jsonify({'msg':'not anyone can view this'})
#
# @app.route('/login')
# def login():
#     auth = request.authorization
#     if auth and auth.password == 'password':
#         token = jwt.encode({'user': auth.username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)},
#                            app.config['SECRET_KEY'])
#         return jsonify(token)
#     return make_response("Couldn't verify", 401, {'WWW-Authenticate': 'Basic realm = "login required'})
#
#
#
# def id_generator():
#     return str(uuid.uuid4().int)[30:]
#
#
# db = client.dbsparta
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
#
# data = requests.get(
#     'https://ticket.interpark.com/ConcertIndex.asp?utm_source=google&utm_medium=cpc&utm_campaign=ticket_concert_20210617_pc_cpc_paidsearch&utm_content=consider_34&utm_term=%EC%BD%98%EC%84%9C%ED%8A%B8&_emk_keyword=%EC%BD%98%EC%84%9C%ED%8A%B8&gclid=Cj0KCQjw39uYBhCLARIsAD_SzMTiWL3pU729Lc47JPjt5zcOhhaMEvhKuSwlt3S4bxOqvXqfSh1Aw2EaAnfwEALw_wcB',
#     headers=headers)
# soup = BeautifulSoup(data.text, 'html.parser')
# title = soup.select('dt.issue_obj');
# for titles in title:
#     singer = titles.select_one('p> span.txt1').text
#     location = titles.select_one('p> span.txt2').text
#     image = titles.select_one('div.thumb> img ')['src']
#     detail_serial = 'https://tickets.interpark.com/goods/'+ titles.select_one('div.thumb> img ')['src'][66:74]
#     doc = {
#         'id': id_generator(),
#         'singer': singer,
#         'location': location,
#         'image': image,
#         'detailPage': detail_serial
#     }
#     if len(list(db.toyproject.find({}))) < 40:
#         db.toyproject.insert_one(doc)
#
#
# @app.route('/home')
# def home():
#     return render_template('index.html')
#
#
# # @app.route('/')
# # def login_page():
# #     return render_template('login.html')
#
#
#
# @app.route('/home/detail')
# def detail_info():
#     data = request.get_json()
#     return jsonify({'msg':data})
#
# # the detail page url = "https://tickets.interpark.com/goods/"+ last 7 digits
#
# # @app.route('/detail', methods=['GET'])
# # def get_popup_info():
# #     url_receive = str(request.form.get('urls_give', False))
# #     print(url_receive)
#
#
# @app.route('/home/data', methods=['GET'])
# def load_homepage():
#     allList = list(db.toyproject.find({}, {'_id': False}))
#     return jsonify({'msg': allList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

