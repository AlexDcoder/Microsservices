from flask import Flask, jsonify, request
import json
import requests


app = Flask(__name__)
data_pecas = []

with open('pecas.json', encoding='utf-8') as pecas_file:
    data_pecas = json.load(pecas_file)

added_products: list = []


@app.route('/carrinho', methods=['GET'])
def default_page():
    return added_products


@app.route('/carrinho/adicionar-produto/<string:id>', methods=['POST'])
def add_product(id):
    new_product = stock_response.get_json()
    added_products.append(new_product)
    return jsonify(new_product)


@app.route('/carrinho/remover-produto/<string:id>')
def remove_product():
    for index, product in enumerate(added_products):
        if id == product['id']:
            del data_pecas[index]
            return data_pecas[index]
    return jsonify({"error": 'Não existe tal produto'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
