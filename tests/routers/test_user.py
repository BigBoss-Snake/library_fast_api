import pytest

from ..test_database import client, test_db


@pytest.mark.webtest()
class TestSignup():

    def test_check_positive_create(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        
        response = client.post('/signup', json=data)

        assert response.status_code == 200

    def test_check_negativ_email(self, test_db):
        data = {
            'email': 'test1test.com',
            'password': 'strings'
        }
        
        response = client.post('/signup', json=data)

        assert response.status_code == 422


    def test_check_negativ_password(self, test_db):
        data = {
            'email': 'test1test.com',
            'password': 'string'
        }
        
        response = client.post('/signup', json=data)

        assert response.status_code == 422

    
    def test_check_used_email(self, test_db):
        data = {
            'email': 'test1test.com',
            'password': 'string'
        }
        response = client.post('/signup', json=data)
        
        response = client.post('/signup', json=data)

        assert response.status_code == 422


    def test_check_create_user(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        check_data = {
            'email': 'test1@test.com',
            'password': 'stringsnotreallyhashed'
        }
        
        response = client.post('/signup', json=data)

        response_data = response.json()
        response_data.pop('id')
        assert response_data == check_data


@pytest.mark.webtest()
class TestSignin():

    def test_check_positive_signin(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)

        response = client.post('/signin', json=data)

        assert response.status_code == 200


    def test_wrong_password(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)
        data_with_wrong_password = {
            'email': 'test1@test.com',
            'password': 'strings1'
        }

        response = client.post('/signin', json=data_with_wrong_password)

        assert response.status_code == 422


    def test_short_password(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)
        data_with_short_password = {
            'email': 'test1@test.com',
            'password': 'string'
        }

        response = client.post('/signin', json=data_with_short_password)

        assert response.status_code == 422


    def test_not_valid_email(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)
        data_with_not_valid_email = {
            'email': 'test1@test.com',
            'password': 'string'
        }

        response = client.post('/signin', json=data_with_not_valid_email)

        assert response.status_code == 422


    def test_wrong_email(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)
        data_with_wrong_email = {
            'email': 'test1test.com',
            'password': 'string'
        }

        response = client.post('/signin', json=data_with_wrong_email)

        assert response.status_code == 422


    def test_check_response_positive_signin(self, test_db):
        data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=data)

        response = client.post('/signin', json=data)

        assert response.json()['email'] == data['email']


