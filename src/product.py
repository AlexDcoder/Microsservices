from flask import Flask, jsonify, request
import json
import requests

app = Flask(__name__)
data_pecas = []

with open('pecas.json', encoding='utf-8') as pecas_file:
    data_pecas = json.load(pecas_file)


@app.route('/produtos', methods=['GET'])
def get_products():
    useful_stock = []
    for peca in data_pecas:
        if peca['quantidade_em_estoque'] > 0:
            useful_stock.append(peca)

    if len(useful_stock) == 0:
        return 'Estoque vazio no momento'

    return useful_stock


@app.route('/produtos/<string:id>', methods=['GET'])
def product_by_id(id):
    for product in data_pecas:
        if id == product['id']:
            return product
    return 'Produto Não Encontrado'


@app.route('/produtos/adicionar-produto', methods=['POST'])
def add_product():
    new_product = request.get_json()
    data_pecas.append(new_product)
    return jsonify(new_product)


@app.route('/produtos/editar-produto/<string:id>', methods=['PUT'])
def edit_product(id):
    edited_product = request.get_json()
    for index, product in enumerate(data_pecas):
        if id == product['id']:
            data_pecas.insert(index, edited_product)
            return jsonify(edited_product)
    return 'Produto Não Encontrado'


@app.route('/produtos/deletar-produto/<string:id>', methods=['DELETE'])
def delet_product(id):
    for index, product in enumerate(data_pecas):
        if product['quantidade_em_estoque'] <= 0:
            del data_pecas[index]
            return data_pecas

        if id == product['id']:
            product['quantidade_em_estoque'] -= 1
            return data_pecas[index]

    return 'Não existe tal produto'


app.run(port=2000, host='localhost', debug=True)
