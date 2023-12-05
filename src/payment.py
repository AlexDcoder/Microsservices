from flask import Flask, request, jsonify
import payment_service
import requests
import json

app = Flask(__name__)

pagamento = [
    {
        "amount": 100,
        "currency": "USD",
        "payment_method": "credit_card",
        "card_number": "1234-5678-9101-1121"
    },
]


@app.route('/initiate_payment', methods=['POST'])
def initiate_payment():
    data = request.json
    response = payment_service.initiate_payment(data)
    return jsonify(response), 200


@app.route('/payment_status/<transaction_id>', methods=['GET'])
def payment_status(transaction_id):
    status = payment_service.check_payment_status(transaction_id)
    return jsonify({"status": status}), 200


app.run(port=4000, host='localhost', debug=True)
