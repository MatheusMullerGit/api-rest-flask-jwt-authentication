import json


def test_post_testuser(app, client):
    mock_request_data = {
        "name":"Teste",
        "username":"userteste",
        "password":"senhateste",
        "email":"teste@gmail.com"
    }
        
    response = client.post('/users', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully registered'
    assert expected in response.get_data(as_text=True)


def test_get_users(app, client):
    response = client.get('/users')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_user_by_name(app, client):
    response = client.get('/users?name=Teste')
    assert response.status_code == 200
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_get_user_by_id(app, client):
    response = client.get('/users/1')
    assert response.status_code == 201
    expected = 'successfully fetched'
    assert expected in response.get_data(as_text=True)


def test_update_testuser(app, client):
    mock_request_data = {
        "name":"Teste updated",
        "username":"userteste",
        "password":"senhateste",
        "email":"teste_updated@gmail.com"
    }
        
    response = client.put('/users/1', json=mock_request_data)
    assert response.status_code == 201
    expected = 'successfully updated'
    assert expected in response.get_data(as_text=True)


def test_delete_user(app, client):
    response = client.delete('/users/1')
    assert response.status_code == 200
    expected = 'successfully deleted'
    assert expected in response.get_data(as_text=True)
