import pytest

from ..test_database import client, test_db


@pytest.mark.webtest()
class TestCreateCategoryArticle():

    def test_positive_create(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
 
        response = client.post('/category_article', json=data, headers=headers)

        assert response.status_code == 201


    def test_check_create_category_article(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/category_article', json=data, headers=headers)
        
        response_data = response.json()
        response_data.pop('id')
        assert response_data == data

    
    def test_create_without_field(self, test_db):
        data = {
            'name': 'string',
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/category_article', json=data, headers=headers)
        
        assert response.status_code == 422


    def test_create_with_wrong_article(self, test_db):
        data = {
            'name': 'string',
            'articles': [125]
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.post('/category_article', json=data, headers=headers)
        
        assert response.status_code == 404


    def test_create_with_article(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        article_data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        response = client.post('/article', json=article_data, headers=headers)
        article_response = response.json()
        article_response.pop('categorys')
        article_response.pop('created_at')
        article_response.pop('update_at')
        data['articles'].append(article_response['id'])

        response = client.post('/category_article', json=data, headers=headers)

        response_data = response.json()
        response_data.pop('id')
        response_data['articles'][0].pop('created_at')
        response_data['articles'][0].pop('update_at')
        data['articles'] = [article_response]
        assert response_data == data


    def test_with_not_valid_access_token(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        headers = {'authorization': '11111'}
        response = client.post('/category_article', json=data, headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
 
        response = client.post('/category_article', json=data)

        assert response.status_code == 422


@pytest.mark.webtest() 
class TestGetArticle():
    
    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)
        category_response = response.json()

        response = client.get(f"/category_article/{category_response['id']}", headers=headers)

        assert response.status_code == 200


    def test_check_article(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)
        category_response = response.json()

        response = client.get(f"/category_article/{category_response['id']}", headers=headers)

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

        response = client.get(f"/category_article/2", headers=headers)

        assert response.status_code == 404

    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.get('/category_article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.get('/category_article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestDeleteCategoryArticle():

    def test_delete_non_existent_category_article(self, test_db):
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.delete(f"/category_article/125", headers=headers)

        assert response.status_code == 404


    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)
        category_response = response.json()

        response = client.delete(f"/category_article/{category_response['id']}", headers=headers)

        assert response.status_code == 204


    def test_check_delete(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
 
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)
        category_response = response.json()
        response = client.delete(f"/article/{category_response['id']}", headers=headers)

        response = client.get(f"/article/{category_response['id']}", headers=headers)

        assert response.status_code == 404

    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.delete('/category_article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.delete('/category_article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestGetArticles():

    def test_check_status(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)

        response = client.get('/category_article', headers=headers)

        assert response.status_code == 200


    def test_len(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)

        response = client.get('/category_article', headers=headers)

        ressponse_data = response.json()
        assert len(ressponse_data) == 1

    
    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        response = client.delete('/category_article/1', headers=headers)

        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.delete('/category_article/1')

        assert response.status_code == 422


@pytest.mark.webtest()
class TestPatchArticle():
    
    def test_positive_patch(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data = {
            'name': 'test',
            'articles': []
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/category_article', json=data, headers=headers)
        category_response = response.json()

        response = client.patch(f"/category_article/{category_response['id']}", json=data, headers=headers)
 
        assert response.status_code == 200


    def test_patch_category(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        update_data = {
            'name': 'test',
            'articles': []
        }
        response = client.post('/category_article', json=data, headers=headers)
        response_category = response.json()
        
        response = client.patch(f"/category_article/{response_category['id']}", json=update_data, headers=headers)

        response_data = response.json()
        response_data.pop('id')
        assert response_data == update_data

    
    def test_create_without_field(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        update_data = {
            'name': 'test'
        }
        response = client.post('/category_article', json=data, headers=headers)
        response_category = response.json()
        
        response = client.patch(f"/category_article/{response_category['id']}", json=update_data, headers=headers)

        response_data = response.json()
        response_data.pop('id')
        update_data['articles'] = []
        assert response_data == update_data


    def test_create_with_wrong_category(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        update_data = {
            'name': 'test',
            'articles': [125]
        }
        response = client.post('/category_article', json=data, headers=headers)
        response_category = response.json()
        
        response = client.patch(f"/category_article/{response_category['id']}", json=update_data, headers=headers)
        
        assert response.status_code == 404


    def test_patch_with_category(self, test_db):
        data = {
            'name': 'string',
            'articles': []
        }
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        update_data = {
            'name': 'test',
            'articles': []
        }
        article_data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}
        response = client.post('/article', json=article_data, headers=headers)
        response_article = response.json()
        update_data['articles'].append(response_article['id'])
        response = client.post('/category_article', json=data, headers=headers)
        response_category = response.json()

        response = client.patch(f"category_article/{response_category['id']}", json=update_data, headers=headers)

        response_article.pop('categorys')
        update_data['articles'] = [response_article]
        response_data = response.json()
        response_data.pop('id')
        
        assert response_data == update_data


    def test_patch_non_existent_category_article(self, test_db):
        data = {
            'name': 'string',
            'articles': [125]
        }
        
        user_data = {
            'email': 'test1@test.com',
            'password': 'strings'
        }
        response = client.post('/signup', json=user_data)
        response = client.post('/signin', json=user_data)
        access_token = response.json()
        headers = {'authorization': access_token['access_token']}

        response = client.patch(f"/category_article/2", json=data, headers=headers)

        assert response.status_code == 404


    def test_with_not_valid_access_token(self, test_db):
        headers = {'authorization': '11111'}
        data = {
            'name': 'string',
            'description': 'string',
            'link': 'string',
            'categorys': []
        }

        response = client.patch('/category_article/1', json=data, headers=headers)
        
        assert response.status_code == 403


    def test_without_access_token(self, test_db):
 
        response = client.patch('/category_article/1')

        assert response.status_code == 422
