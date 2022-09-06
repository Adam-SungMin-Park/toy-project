from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import uuid

app = Flask(__name__)



client = MongoClient('mongodb+srv://test:sparta@cluster0.o2cbi29.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     UuidRepresentation="standard")
db = client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://ticket.interpark.com/ConcertIndex.asp?utm_source=google&utm_medium=cpc&utm_campaign=ticket_concert_20210617_pc_cpc_paidsearch&utm_content=consider_34&utm_term=%EC%BD%98%EC%84%9C%ED%8A%B8&_emk_keyword=%EC%BD%98%EC%84%9C%ED%8A%B8&gclid=Cj0KCQjw39uYBhCLARIsAD_SzMTiWL3pU729Lc47JPjt5zcOhhaMEvhKuSwlt3S4bxOqvXqfSh1Aw2EaAnfwEALw_wcB', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select('dt.issue_obj');
for titles in title:
    singer = titles.select_one('p> span.txt1').text
    location = titles.select_one('p> span.txt2').text
    image = titles.select_one('div.thumb> img ')['src']
    doc = {
        'singer': singer,
        'location': location,
        'image': image
    }
    db.toyproject.insert_one(doc)


#Hot_0_On > div > a > img
@app.route('/')
def home():
    return render_template('index.html')


#@app.route('/', methods = ['GET'])
#def load_homepage():



@app.route('/more_info')
def more_info():
    return render_template('moreInfo.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
