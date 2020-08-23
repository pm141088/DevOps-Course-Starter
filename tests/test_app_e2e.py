import pytest
import os
from threading import Thread
from selenium import webdriver

import trello_items
import app

@pytest.fixture(scope='module')
def test_app():
    # Create the new board & update the board id environment variable
    board_id = trello_items.create_trello_board("TEST BOARD")
    os.environ['TRELLO_BOARD_ID'] = board_id

    # construct the new application
    application = app.create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear Down
    thread.join(1)
    trello_items.delete_trello_board(board_id)

@pytest.fixture(scope='module')
def driver():
    # path to your webdriver download
    with webdriver.Chrome('C:\Work\DevOps-Course-Starter\drivers\chromedriver.exe') as driver:
        yield driver

def test_app_home(driver, test_app):
    driver.get('http://localhost:5000')
    assert driver.title == 'To-Do App'