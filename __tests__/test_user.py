# 1 - Incluir, consultar, alterar e excluir um usuário, sempre com o teste do Status Code
#  e pelo menos 3 testes de campos

# Bibliotecas
import json
import pytest
import requests

from utils.utils import ler_csv

# Dados comuns
url_user = 'https://petstore.swagger.io/v2/user'
headers = {'Content-Type': 'application/json'}

# Dados  usuário
user_id = 151174808
username = "Nina Lima"
first_name = "Nina"
last_name = "Saudade"
email = "nina_saudade@gmail.com"
password = "123saudade"
phone = "99878-2563"

# Função de inclusão de usuário (POST)
def test_post_user():
    user_data = {
        "id": user_id,
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": 1
    }
    
    response = requests.post(
        url=url_user,
        headers=headers,
        data=json.dumps(user_data),
        timeout=5
    )

    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)


# Função de consulta de usuário (GET)
def test_get_user():
    response = requests.get(
        url=f'{url_user}/{username}',
        headers=headers
    )
    
    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['id'] == user_id
    assert response_body['username'] == username
    assert response_body['firstName'] == first_name
    assert response_body['email'] == email

# Função de atualização de usuário (PUT)
def test_put_user():
    updated_user_data = {
    "id": 151174808,
    "username": "Nina Lima",
    "firstName": "Nina",
    "lastName": "Saudade",
    "email": "nina_saudade@gmail.com",
    "password": "123saudade",
    "phone": "99878-2563",
    "userStatus": 1
    }
    
    response = requests.put(
        url=f'{url_user}/{username}',
        headers=headers,
        data=json.dumps(updated_user_data),
        timeout=5
    )
    
    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)


# Função de exclusão de usuário (DELETE)
def test_delete_user():
    response = requests.delete(
        url=f'{url_user}/{username}',
        headers=headers,
        timeout=5
    )
    
    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == username



# 3 - Altere a função Post e Delete da entidade User para que executem os testes a partir de uma massa com json dinamico
    

@pytest.mark.parametrize('user_id,username,first_name,last_name,email,password,phone,user_status', 
                         ler_csv('./fixtures/csv/user.csv'))
def test_post_user_dinamico(user_id, username, first_name, last_name, email, password, phone, user_status):
    # Preparar os dados do usuário
    user_data = {
        "id": int(user_id),
        "username": username,
        "firstName": first_name,
        "lastName": last_name,
        "email": email,
        "password": password,
        "phone": phone,
        "userStatus": int(user_status)
    }

    # Fazer a requisição POST
    response = requests.post(
        url=url_user,
        headers=headers,
        data=json.dumps(user_data),
        timeout=5
    )

    # Validação de resposta
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == str(user_id)









