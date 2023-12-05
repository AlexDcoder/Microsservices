def initiate_payment(data):
    # Aqui você inclui a lógica para iniciar um pagamento.
    # Isso pode incluir a validação dos dados de pagamento,
    # a comunicação com um gateway de pagamento externo, etc.
    return {"transaction_id": "12345", "status": "pending"}


def check_payment_status(transaction_id):
    # Aqui você inclui a lógica para verificar o status do pagamento.
    # Isso pode envolver consultar o banco de dados ou o gateway de pagamento.
    return "completed"  # Exemplo
