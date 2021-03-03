import pytest
import requests
import json

from dotenv import find_dotenv, load_dotenv
from app import create_app
from entity.item import Item

@pytest.fixture
def client():
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    
    # Create the new app.
    test_app = create_app()
    
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

def stub_get_db_collection():
    return

def stub_get_all_items(collection):
    return [
        Item(
            'test-to-do-item-id',
            'Test To Do item Title',
            'To Do',
            'Test To Do item Description',
            '2020-07-30T12:52:06.278Z'
        ),
        Item(
            'test-doing-item-id',
            'Test Doing item Title',
            'Doing',
            'Test Doing item Description',
            '2020-07-30T12:52:06.278Z'
        ),
        Item(
            'test-done-item-id',
            'Test Done item Title',
            'Done',
            'Test Done item Description',
            '2020-07-30T12:52:06.278Z'
        )
    ]

def test_app(monkeypatch, client):
    monkeypatch.setattr(
        'app.get_db_collection',
        stub_get_db_collection
    )
    monkeypatch.setattr(
        'app.get_all_items',
        stub_get_all_items
    )

    response = client.get('/')
    
    content = str(response.data)
    print (content)
    assert response.status_code == 200 
    assert 'Test To Do item Title' in content
    assert 'Test Doing item Title' in content
    assert 'Test Done item Title' in content