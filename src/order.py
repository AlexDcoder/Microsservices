from flask import Flask, request, jsonify
import payment_service
import requests
import json


app = Flask(__name__)
pedidos: list = []


@app.route('/pedido', methods=['GET'])
def listar_pedidos():
    return jsonify(pedidos)


@app.route('/pedido/add-carrinho', methods=['POST'])
def adicionar_pedido():
    try:
        cart_response = requests.get('http://localhost:5000/carrinho')
        cart_response.raise_for_status()
        if len(cart_response.json()) != 0:
            novo_pedido = cart_response.json()
            pedidos.append(novo_pedido)
            return novo_pedido

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/pedido/<int:pedido_id>', methods=['GET'])
def buscar_pedido(pedido_id):
    pedido = [p for id, p in enumerate(pedidos) if id == pedido_id]
    if pedido:
        return jsonify(pedido)
    else:
        return jsonify({'mensagem': 'Pedido não encontrado'}), 404


if __name__ == '__main__':
    app.run(port=3000, host='localhost', debug=True)
