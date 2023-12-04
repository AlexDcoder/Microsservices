from flask import Flask, jsonify, request
import json


ecommerce = Flask(__name__)
data_users = []
data_pecas = []

with open('usuarios.json', encoding='utf-8') as user_file:
    data_users = json.load(user_file)

with open('pecas.json', encoding='utf-8') as pecas_file:
    data_pecas = json.load(pecas_file)


@ecommerce.route('/', methods=['GET'])
def default_page():
    return '''
    Welcome
    to the
    Application of
    "F no chat"
    '''


ecommerce.run(port=5000, host='localhost', debug=True)
