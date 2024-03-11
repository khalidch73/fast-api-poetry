import requests
# test 1
response = requests.get('http://127.0.0.1:8000')
def test_status_code_main_route ():
    assert response.status_code == 200
# test 2
response1 = requests.get('http://127.0.0.1:8000/status')
def test_status_code_status_route ():
    assert response1.status_code == 200
# test 3
response2 = requests.get('http://127.0.0.1:8000/hello')
def test_status_code_hello_user_route ():
    assert response2.status_code == 200
# test 4
response3 = requests.get('http://127.0.0.1:8000/hello/{name}')
def test_status_code_hello_user_name_route ():
    assert response3.status_code == 200

response4 = requests.post('http://127.0.0.1:8000/create_user/', json= {
  "msg": "we got data succesfully",
  "user_id": 1,
  "username": "waleed",
  "password": "12331dada"
})
def test_status_code_user_data ():
    assert response4.status_code == 200