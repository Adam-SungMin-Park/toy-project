from flask import Flask, render_template, request, jsonify
from bs4 import BeautifulSoup
from pymongo import MongoClient
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import requests
import uuid

app = Flask(__name__)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


# try:
#     all_list = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.CLASS_NAME, 'contents'))
#     )
#     print(all_list)
#     driver.quit()
# except:
#     driver.quit()


# this can be used for the detailed page


def id_generator():
    return str(uuid.uuid4().int)[30:]


client = MongoClient('mongodb+srv://test:sparta@cluster0.o2cbi29.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     UuidRepresentation="standard")
db = client.dbsparta
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(
    'https://ticket.interpark.com/ConcertIndex.asp?utm_source=google&utm_medium=cpc&utm_campaign=ticket_concert_20210617_pc_cpc_paidsearch&utm_content=consider_34&utm_term=%EC%BD%98%EC%84%9C%ED%8A%B8&_emk_keyword=%EC%BD%98%EC%84%9C%ED%8A%B8&gclid=Cj0KCQjw39uYBhCLARIsAD_SzMTiWL3pU729Lc47JPjt5zcOhhaMEvhKuSwlt3S4bxOqvXqfSh1Aw2EaAnfwEALw_wcB',
    headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

title = soup.select('dt.issue_obj');
for titles in title:
    singer = titles.select_one('p> span.txt1').text
    location = titles.select_one('p> span.txt2').text
    image = titles.select_one('div.thumb> img ')['src']
    doc = {
        'id': id_generator(),
        'singer': singer,
        'location': location,
        'image': image
    }
    detail_serial = image[66:74]
for numbers in detail_serial:
    detail_data = requests.get('https://tickets.interpark.com/goods/' + numbers)
    second_soup = BeautifulSoup(detail_data.text, 'html.parser')
    location = second_soup.select_one(
        '#container > div.contents > div.productWrapper > div.productMain > div.productMainTop > div > div.summaryBody > ul > li:nth-child(2) > div > p')
    print(location)
#     # STOPPED HERE. TRY USING SELENIUM TO RETRIEVE JS DATA

if len(list(db.toyproject.find({}))) < 40:
    db.toyproject.insert_one(doc)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/detail')
def more_info():
    return render_template('moreInfo.html')


# the detail page url = "https://tickets.interpark.com/goods/"+ last 7 digits

@app.route('/popup', methods=['GET'])
def get_popup_info():
    url_receive = request.form('url_give')
    print(url_receive)
    if url_receive is not "":
        print(url_receive)
        driver.get('https://tickets.interpark.com/goods/' + url_receive)
    try:
        all_list = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'contents'))
        )
        return jsonify(all_list.text)
        driver.quit()
    except:
        driver.quit()

    # detail_data = requests.get('https://tickets.interpark.com/goods/' + url_receive, headers=headers)
    # return detail_data


@app.route('/home', methods=['GET'])
def load_homepage():
    allList = list(db.toyproject.find({}, {'_id': False}))
    return jsonify({'msg': allList})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
