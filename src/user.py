import time
from flask import Flask, request, jsonify, request
import json
import requests
import validate_credentials

app = Flask(__name__)
data_users = []

with open('usuarios.json', encoding='utf-8') as users_files:
    data_users = json.load(users_files)


@app.route('/user/<string:name>', methods=['GET'])
def initial_page(name):

    return f'''
    Digite na url:
        '/validate_user' => Para validar usuário {name}
        '/product' => Para ver lista de produtos
        '/product/detail/id do produto' => Para ver detalhes de um produto
        '/carrinho' => Para ver carrinho
        '/carrinho/product/<string:id>' => Para ver detalhes de um produto de um carrinho
        '/iniciar/pagamento' => Para ver detalhes de um produto de um carrinho
    '''

# DONE


@app.route('/user/<string:name>/validate_user', methods=['GET'])
def validate_user(name):
    result = validate_credentials.check_user_credentials(name, data_users)
    return jsonify({"name": f"{name}",
                    "is_valid": result})

# TODO


@app.route('/user/<string:name>/product', methods=['GET'])
def see_product(name):
    pass

# TODO


@app.route('/user/<string:name>/product/detail/<string:id>', methods=['POST'])
def see_product_detail(name, id):
    pass


@app.route('/user/<string:name>/carrinho', methods=['GET'])
def see_cart(name):
    pass


# TODO
@app.route('/user/<string:name>/carrinho/product/<string:id>', methods=['GET'])
def see_cart_product_detail(name, id):
    pass


# TODO
@app.route('/user/<string:name>/initiate_payment', methods=['POST'])
def start_payment(name):
    pass


if __name__ == '__main__':
    app.run(port=1000, host='localhost', debug=True)
