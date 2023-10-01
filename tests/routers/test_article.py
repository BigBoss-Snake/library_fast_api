import pytest

from ..test_database import client, test_db


@pytest.mark.webtest()
class TestCreateArticle():

    def test_positive_create(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
 
        response = client.post('/article', json=data, headers=headers)

        assert response.status_code == 201


    def test_check_create_article(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/article', json=data, headers=headers)
        
        response_data = response.json()
        response_data.pop('id')
        response_data.pop('created_at')
        response_data.pop('update_at')
        assert response_data == data

    
    def test_create_without_field(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/article', json=data, headers=headers)
        
        assert response.status_code == 422


    def test_create_with_wrong_category(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': [1]
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/article', json=data, headers=headers)
        
        assert response.status_code == 404


    def test_create_with_category(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        category_data = {'name': 'Test', 'articles': []}
        response = client.post('/category_article', json=category_data, headers=headers)
        category_response = response.json()
        category_response.pop('articles')
        data['categorys'].append(category_response['id'])

        response = client.post('/article', json=data, headers=headers)

        response_data = response.json()
        response_data.pop('id')
        response_data.pop('created_at')
        response_data.pop('update_at')
        data['categorys'] = [category_response]
        assert response_data == data


    def test_with_not_valid_access_token(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        headers = {'authorization': '11111'}
        response = client.post('/article', json=data, headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
 
        response = client.post('/article', json=data)

        assert response.status_code == 422


@pytest.mark.webtest() 
class TestGetArticle():
    
    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.get(f"/article/{article_response['id']}", headers=headers)

        assert response.status_code == 200


    def test_check_article(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.get(f"/article/{article_response['id']}", headers=headers)

        assert response.status_code == 200


    def test_get_non_existent_article(self, test_db):
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.get(f"/article/2", headers=headers)

        assert response.status_code == 404

    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.get('/article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.get('/article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestDeleteArticle():

    def test_delete_non_existent_article(self, test_db):
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.delete(f"/article/2", headers=headers)

        assert response.status_code == 404


    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.delete(f"/article/{article_response['id']}", headers=headers)

        assert response.status_code == 204


    def test_check_delete(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
 
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()
        response = client.delete(f"/article/{article_response['id']}", headers=headers)

        response = client.get(f"/article/{article_response['id']}", headers=headers)

        assert response.status_code == 404

    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.delete('/article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.delete('/article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestGetArticles():

    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)

        response = client.get('/article', headers=headers)

        assert response.status_code == 200


    def test_len(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)

        response = client.get('/article', headers=headers)

        ressponse_data = response.json()
        assert len(ressponse_data) == 1

    
    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.delete('/article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.delete('/article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestPatchArticle():
    
    def test_positive_patch(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.patch(f"/article/{article_response['id']}", json=data, headers=headers)
 
        assert response.status_code == 200


    def test_check_patch_article(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data ={
            'name': 'Test',
            'description': 'Test',
            'link': 'Test',
            'categorys': []
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.patch(f"article/{article_response['id']}", json=update_data, headers=headers)
        
        response_data = response.json()
        response_data.pop('id')
        response_data.pop('created_at')
        response_data.pop('update_at')
        assert response_data == update_data

    
    def test_patch_without_field(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data ={
            'name': 'Test',
            'link': 'Test',
            'categorys': []
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.patch(f"article/{article_response['id']}", json=update_data, headers=headers)
        
        response_data = response.json()
        response_data.pop('id')
        response_data.pop('created_at')
        response_data.pop('update_at')
        response_data.pop('description')
        assert response_data == update_data


    def test_patch_with_wrong_category(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data ={
            'name': 'Test',
            'link': 'Test',
            'description': 'Test',
            'categorys': [1]
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=data, headers=headers)
        article_response = response.json()

        response = client.patch(f"article/{article_response['id']}", json=update_data, headers=headers)
        
        assert response.status_code == 404


    def test_patch_with_category(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data = {
            'categorys': []
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        category_data = {'name': 'Test', 'articles': []}
        response = client.post('/category_article', json=category_data, headers=headers)
        category_response = response.json()
        category_response.pop('articles')
        update_data['categorys'].append(category_response['id'])
        response = client.post('/article', json=data, headers=headers)
        article_reponse = response.json()

        response = client.patch(f"article/{article_reponse['id']}", json=update_data, headers=headers)

        response_data = response.json()
        response_data.pop('id')
        response_data.pop('created_at')
        response_data.pop('update_at')
        data['categorys'] = [category_response]
        assert response_data == data


    def test_patch_non_existent_article(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': [1]
        }
        
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.patch(f"/article/2", json=data, headers=headers)

        assert response.status_code == 404


    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }

        response = client.patch('/article/1', json=data, headers=headers)
        
        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.patch('/article/1')

        assert response.status_code == 422
