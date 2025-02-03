from http import HTTPStatus
from django.urls import reverse
import pytest
from django.contrib.auth.models import User, Permission
from contacts.models import Contact


def test_contacts_thanks(client):
    #Given
    name = 'Jonh'

    #When
    response = client.get(reverse("contacts:thanks", args=(name,)))

    #Then
    assert response.status_code == HTTPStatus.OK
    # o decode serve para converter bytes para string, e assim comparar usando o assert
    assert response.content.decode() == f"Obrigado por preencher o formulário, {name}" 


def test_contact_create_with_unauthenticated_user_succes(client):
    
    # Given
    url = f'{reverse("accounts:login")}?next={reverse("contacts:create")}'

    # When
    response = client.get(reverse("contacts:create"))

    # Then
    assert response.status_code == HTTPStatus.FOUND
    assert response.url == url


@pytest.mark.django_db
def test_contact_create_success(client, django_user_model):
    # Given
    data = {
        'subject': 'Test Subject',
        'message': 'This is a test message.',
        'sender': 'test@example.com',
        'cc_myself': True
    }

    user = django_user_model.objects.create_user(username='john', email='john@testmail.com', password='123mudar')
    permission = Permission.objects.get(codename='add_contact')
    user.user_permissions.add(permission)
    
    client.force_login(user)

    # When
    response = client.post(reverse("contacts:create"), data)

    # Then
    assert response.status_code == HTTPStatus.FOUND  # Verifica se o status é 302 (redirecionamento)
    assert Contact.objects.filter(sender="test@example.com").exists()

