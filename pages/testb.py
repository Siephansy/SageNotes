import requests

webhook_url = "http://127.0.0.1:5678/webhook-test/7109995a-fbfa-4b8a-8049-8ee62622d853"  # COLOQUE A SUA URL DO N8N AQUI

try:
    response = requests.post(webhook_url)
    if response.status_code == 200:
        print("Teste de conexão bem-sucedido com teste_conexao.py!")
        print("Resposta do servidor:")
        print(response.text)
    else:
        print(f"Erro no teste de conexão com teste_conexao.py. Código de estado: {response.status_code}")
        print("Resposta de erro do servidor:")
        print(response.text)
except requests.ConnectionError as e:
    print(f"Erro de conexão com teste_conexao.py: {e}")