import json
import random


def gerar_json_pecas_aleatorias(num_pecas=100):
    pecas = []

    for _ in range(num_pecas):
        nome = random.choice(
            ["CPU", "Memória RAM", "Placa de Vídeo", "HD", "SSD",
             "Placa Mãe", "Gabinete", "Cooler", "Fonte"])
        qualidade = random.choice(["Baixa", "Média", "Alta"])
        preco = round(random.uniform(100, 2000), 2)
        quantidade_em_estoque = random.randint(1, 100)

        peca = {
            "nome": nome,
            "qualidade": qualidade,
            "preco": preco,
            "quantidade_em_estoque": quantidade_em_estoque
        }

        pecas.append(peca)

    with open('pecas.json', 'w', encoding='utf-8') as json_file:
        json.dump(pecas, json_file, indent=2)


# Gerando e salvando o JSON em um arquivo
gerar_json_pecas_aleatorias()
