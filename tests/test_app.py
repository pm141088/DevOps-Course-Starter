import pytest
from dotenv import find_dotenv, load_dotenv
import requests
import app

@pytest.fixture
def client():
    # Use our test integration config instead of the 'real' version
    file_path = find_dotenv('.env.test')
    load_dotenv(file_path, override=True)
    # Create the new app.
    test_app = app.create_app()
    # Use the app to create a test_client that can be used in our tests.
    with test_app.test_client() as client:
        yield client

class MockCardsResponse:
    def json():
        return [
            {
                "id": "5ef7a4f991ad48544d0f2a53",
                "idList": "todo_list_id",
                "name": "This is a to do item",
                "desc": "Description for to do item",
                "dateLastActivity": "2020-07-30T12:52:06.278Z"
            },
            {
                "id": "5ef7a4f991ad48544d0f2a54",
                "idList": "doing_list_id",
                "name": "This item is currently in progress",
                "desc": "Description for item in progress",
                "dateLastActivity": "2020-07-30T12:52:06.278Z"
            },
            {
                "id": "5ef7a4f991ad48544d0f2a55",
                "idList": "done_list_id",
                "name": "This item is done",
                "desc": "Description for done item",
                "dateLastActivity": "2020-07-30T12:52:06.278Z"
            },
        ]

@pytest.fixture()
def mock_get_requests(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockCardsResponse

    monkeypatch.setattr(requests, "request", mock_get)


def test_app(mock_get_requests, client):
    # mock_get_requests.get("https://api.trello.com/1/boards/board_id/cards", json={})
    response = client.get('/')
    assert response.status_code == 200 

    html_string = str(response.data)
    assert 'This is a to do item' in html_string
    assert 'This item is currently in progress' in html_string
    assert 'This item is done' in html_string