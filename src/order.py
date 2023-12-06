from flask import Flask, request, jsonify
import payment_service
import requests
import json


app = Flask(__name__)
pedidos: list = []


@app.route('/pedido', methods=['GET'])
def listar_pedidos():
    return jsonify(pedidos)


@app.route('/pedido/add-carrinho/', methods=['POST'])
def adicionar_carrinho():
    novo_pedido = request.get_json()
    pedidos.append(novo_pedido)
    return jsonify(novo_pedido)


@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def buscar_pedido(pedido_id):
    pedido = next((p for p in pedidos if p['id'] == pedido_id), None)
    if pedido:
        return jsonify(pedido)
    else:
        return jsonify({'mensagem': 'Pedido não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)
