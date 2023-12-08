from itertools import product
import time
from flask import Flask, request, jsonify, request
import json
import requests
import validate_credentials


app = Flask(__name__)
data_users = []

with open('usuarios.json', encoding='utf-8') as users_files:
    data_users = json.load(users_files)


@app.route('/user', methods=['GET'])
def initial_page():

    return f'''
    Digite na url:
        'um nome de usuário/validate_user' => Para validar usuário com tal nome
        '/product' => Para ver lista de produtos
        '/product/detail/id do produto' => Para ver detalhes de um produto

        '/carrinho' => Para ver carrinho
        '/carrinho/product/id' => Para ver detalhes de um produto de um carrinho
        '/carrinho/carrinho/add/id' => Para adicionar um produto de um carrinho
        '/carrinho/carrinho/rem/id' => Para remover um produto de um carrinho

        '/pedido/' => Para ver os pedidos
        '/pedido/add' => Para adicionar carrinho aos pedidos

        '/iniciar/pagamento' => Para iniciar um pagamento
    '''

# DONE


@app.route('/user/<string:name>/validate_user', methods=['GET'])
def validate_user(name):
    result = validate_credentials.check_user_credentials(name, data_users)
    return jsonify({"name": f"{name}",
                    "is_valid": result})

# TODO


@app.route('/user/product', methods=['GET'])
def see_product():
    try:

        response = requests.get('http://localhost:2000/products', timeout=5)
        response.raise_for_status()
        product_list = response.json()
        return jsonify(product_list)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# TODO


@app.route('/user/product/detail/<string:id>', methods=['GET'])
def see_product_detail(id):
    try:
        response = requests.get(f'http://localhost:2000/products/{id}')
        response.raise_for_status()
        product_detail = response.json()
        return jsonify(product_detail)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# TODO


@app.route('/user/carrinho', methods=['GET'])
def see_cart():
    try:

        response = requests.get(f'http://localhost:5000/carrinho')
        response.raise_for_status()
        cart = response.json()
        return jsonify(cart)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/carrinho/product/<string:id>', methods=['GET'])
def see_cart_product_detail(id):
    try:

        response = requests.get(f'http://localhost:5000/carrinho/{id}')
        response.raise_for_status()
        cart = response.json()
        return jsonify(cart)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/carrinho/add/<string:id>', methods=['GET'])
def add_to_cart(id):
    try:

        response = requests.post(
            f'http://localhost:5000/carrinho/adicionar-produto/{id}')
        response.raise_for_status()
        cart_add_product = response.json()
        return jsonify(cart_add_product)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/carrinho/rem/<string:id>', methods=['GET'])
def remove_from_cart(id):
    try:

        response = requests.delete(
            f'http://localhost:5000/carrinho/remover-produto/{id}')
        response.raise_for_status()
        updated_list = response.json()
        return jsonify(updated_list)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/pedido', methods=['GET'])
def see_order():
    try:

        response = requests.get(f'http://localhost:3000/pedido')
        response.raise_for_status()
        order = response.json()
        return jsonify(order)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/user/pedido/<int:id>', methods=['GET'])
def see_order_detail(id):
    try:

        response = requests.get(f'http://localhost:3000/pedido/{id}')
        response.raise_for_status()
        order = response.json()
        return jsonify(order)

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# TODO
@app.route('/user/initiate_payment', methods=['POST'])
def start_payment():
    try:

        response = requests.post(
            f'http://localhost:4000/initiate_payment')

        response.raise_for_status()

        return jsonify(response.json())

    except requests.Timeout:
        return jsonify({"error": "Request to the target API timed out"}), 500
    except requests.RequestException as e:
        return jsonify({"error": f"Request to the target API failed. {str(e)}"}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(port=1000, host='localhost', debug=True)
