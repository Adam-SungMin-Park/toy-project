from flask import Flask, render_template, request, jsonify
import uuid

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://test:sparta@cluster0.o2cbi29.mongodb.net/Cluster0?retryWrites=true&w=majority',
                     UuidRepresentation="standard")
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/more_info')
def more_info():
    return render_template('moreInfo.html')


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
