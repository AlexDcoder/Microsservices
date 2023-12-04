import json
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_user():
    user = {
        "nome": generate_random_string(8),
        "email": f"{generate_random_string(8)}@example.com",
        "idade": random.randint(18, 60),
        "ativo": random.choice([True, False]),
        "saldo": round(random.uniform(100.0, 1000.0), 2)
    }
    return user


def generate_users(num_users):
    users = [generate_user() for _ in range(num_users)]
    return users


def save_to_json(users, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=2, ensure_ascii=False)


# Gerar 5 usuÃ¡rios e salvar no arquivo "usuarios.json"
num_users = 100
usuarios_data = generate_users(num_users)
save_to_json(usuarios_data, 'usuarios.json')
