# Bibliotecas
import json
import pytest
import requests

# Dados comuns
url_order = 'https://petstore.swagger.io/v2/store/order'
headers = {'Content-Type': 'application/json'}

# Dados do pedido
order_id = 1212        # ID do pedido que será criado
pet_id = 151174809     # ID do pet do  pedido
quantity = 1           # Quantidade do pet no pedido
status = "placed"      # Status do pedido ( placed= colocado/colocada )

# Função de incluir  pedido (POST)
def test_post_order():
    order_data = {
        "id": order_id,
        "petId": pet_id,
        "quantity": quantity,
        "shipDate": "2024-11-05T00:08:51.134Z",  # Data do envio
        "status": status,
        "complete": True        # true verdadeiro/verdadeira 
    }
    
    response = requests.post(url=url_order, headers=headers, data=json.dumps(order_data), timeout=5)

    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['petId'] == pet_id
    assert response_body['quantity'] == quantity
    assert response_body['status'] == status

# Função de consulta de pedido (GET)
def test_get_order():
    response = requests.get(url=f'{url_order}/{order_id}', headers=headers)
    
    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['petId'] == pet_id
    assert response_body['quantity'] == quantity
    assert response_body['status'] == status

# Função de exclusão de pedido (DELETE)
def test_delete_order():
    response = requests.delete(url=f'{url_order}/{order_id}', headers=headers, timeout=5)
    
    # Validação de resposta
    assert response.status_code == 200

    # Verifica se o pedido foi realmente excluído
    get_response = requests.get(url=f'{url_order}/{order_id}', headers=headers)
    assert get_response.status_code == 404         # Pedido não deve mais existir

