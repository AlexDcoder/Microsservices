from itertools import product
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


@app.route('/carrinho/<string:id>', methods=['GET', 'POST'])
def see_product_details_in_cart(id: str):
    try:
        stock_response = requests.get(f'http://localhost:2000/products/{id}')
        stock_response.raise_for_status()
        return jsonify(stock_response.json())
    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/carrinho/adicionar-produto/<string:id>', methods=['POST'])
def add_product(id: str):
    try:
        stock_response = requests.get(f'http://localhost:2000/products/{id}')
        stock_response.raise_for_status()
        new_product = stock_response.json()
        added_products.append(new_product)
        return jsonify(new_product)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/carrinho/remover-produto/<string:id>', methods=['DELETE'])
def remove_product(id):
    for index, product in enumerate(added_products):
        if id == product['id']:
            del added_products[index]
            return 'Produto Removido'
    return jsonify({"error": 'Não existe tal produto'})


if __name__ == '__main__':
    app.run(port=5000, host='localhost', debug=True)
