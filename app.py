# -*- coding: UTF-8 -*-
from wechat_work_helper import send_textmessage
from flask import Flask,request,jsonify,abort
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/send2wechat/api/v1/mstodo', methods=['POST'])
def sendmstodo():
    if not request.json or not 'subject' or not 'time' in request.json:
        abort(400)
    postcontent='N/A'
    if ('content' in request.json):
        content=request.json['content']
    textmessage = request.json['time'] + '\n' + request.json['subject'] + '\n' + postcontent
    task = send_textmessage(textmessage)
    return jsonify({'task': task}), 201

