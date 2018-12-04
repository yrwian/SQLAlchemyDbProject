#!flask/bin/python
from flask import Flask, jsonify
from flask import request
import json

from common.jsonutils import JsonUtils
from model.user import User
from db.dbmanager import DbManager

app = Flask(__name__)


# 根据关键字模糊搜索用户
@app.route('/v1.0/api/users', methods=['GET'])
def get_users():
    keywords = request.args.get('keywords')
    try:
        users = DbManager().queryByKeywords(keywords)
        return jsonify({'code': 0, 'users': users})
    except Exception as e:
        print(e)
        return jsonify({'code': -1, 'msg': '请求失败！', 'error': e.__str__()})


# 添加一条数据到数据库
@app.route('/v1.0/api/users', methods=['POST'])
def add_users():
    manager = DbManager()
    try:
        utils = JsonUtils()
        city = utils.json2obj(request.get_json(), User())
        manager.addUser(city)
        return jsonify({'code': 0, 'users': manager.query()})
    except Exception as e:
        manager.mySession.rollback()
        print(e)
        return jsonify({'code': -1, 'msg': '请求失败！', 'error': e.__str__()})


if __name__ == '__main__':
    app.run(debug=True)
