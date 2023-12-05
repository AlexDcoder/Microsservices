import json
import random
import string


def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))


def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password


def generate_user():
    user = {
        "nome": generate_random_string(random.randint(5, 8)),
        "email": f"{generate_random_string(8)}@example.com",
        "idade": random.randint(18, 60),
        "ativo": random.choice([True, False]),
        "password": f"{generate_random_password(random.randint(5, 8))}",
        "saldo": round(random.uniform(100.0, 1000.0), 2)
    }
    return user


def generate_users(num_users):
    users = [generate_user() for _ in range(num_users)]
    return users


def save_to_json(users, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(users, file, indent=2, ensure_ascii=False)


NUM_USERS = 5
usuarios_data = generate_users(NUM_USERS)
save_to_json(usuarios_data, 'usuarios.json')
