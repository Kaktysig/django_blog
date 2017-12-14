import pytest

from django.shortcuts import get_object_or_404
from blog.models import Articles
from django.contrib.auth.models import User

def create_test_user():
    u1 = User.objects.create_user(username='UserName', password='Password123', email='Test@gmail.com')
    return u1

@pytest.mark.django_db
def test_list_view(client):
    response = client.get('/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_article(client):
    u1 = create_test_user()
    client.force_login(u1)

    test_name = 'test'
    client.post('/create/', {
        'name' : test_name,
        'content' : test_name,
    })

    obj = Articles.objects.get(name=test_name)
    assert obj.id > 0

@pytest.mark.django_db
def test_delete_article(client):
    u1 = create_test_user()
    client.force_login(u1)

    test_name = 'test'
    client.post('/create/', {
        'name': test_name,
        'content': test_name,
    })
    obj = Articles.objects.get(name=test_name)

    address = '/delete/' + str(obj.id) + '/'
    client.post(address)
    try:
        get_object_or_404(Articles, id=obj.id)
    except Exception as e:
        assert e.args[0] == "No Articles matches the given query."


@pytest.mark.django_db
def test_edit_article(client):
    u1 = create_test_user()
    client.force_login(u1)

    test_name = 'test'
    client.post('/create/', {
        'name': test_name,
        'content': test_name,
    })
    obj = Articles.objects.get(name=test_name)

    edit_name = 'another_test_name'
    client.post('/update/' + str(obj.id) + '/', {
        'name': edit_name,
        'content': test_name,
    })

    new_obj = Articles.objects.get(id=obj.id)

    assert new_obj.name == edit_name

# 85% покрытия есть. Дальше увы не успеваю :(
