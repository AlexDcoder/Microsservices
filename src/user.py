from flask import Flask, request, jsonify

app = Flask(__name__)


def check_user_credentials(id: str, password: str):
    if len(id) < 5 or len(password) < 6:
        return False
    return True


@app.route('/validate_user', methods=['POST'])
def validate_user():
    data = request.get_json()
    user_id = data.get('user_id')
    password = data.get('password')

    is_valid = check_user_credentials(user_id, password)

    return jsonify({"is_valid": is_valid})


app.run(port=1000, host='localhost', debug=True)
