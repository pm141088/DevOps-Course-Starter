import pytest
import os
import requests
import logging
import uuid

from threading import Thread
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from dotenv import find_dotenv, load_dotenv
from app import create_app
from mongo_db.index import get_db_collection
from entity.status import Status

log = logging.getLogger('app')

@pytest.fixture(scope='module')
def test_app():
    file_path = find_dotenv()
    load_dotenv(file_path, override=True)

    os.environ['LOGIN_DISABLED'] = 'True'

    # Create a temporary mongoDB test collection
    os.environ['MONGO_DB_DATABASE_NAME'] = f'{uuid.uuid4()}'
    collection = get_db_collection() 
    
    # Drop the collection in case there is data in there already
    collection.drop()

    # Create the new app
    application = create_app()

    # start the app in its own thread.
    thread = Thread(target=lambda: application.run(use_reloader=False))
    thread.daemon = True
    thread.start()
    yield application

    # Tear down app and test collection
    thread.join(1)
    collection.drop()


@pytest.fixture(scope='module')
def driver():
    opts = webdriver.ChromeOptions()
    opts.add_argument('--headless')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-dev-shm-usage')
    with webdriver.Chrome('./chromedriver', options=opts) as driver:
        yield driver

def test_task_journey(driver, test_app):
    driver.implicitly_wait(3)
    driver.get('http://localhost:5000/')
    assert driver.title == 'To-Do App'

    # Create a new item
    add_item_input = driver.find_element_by_name("item_title")
    add_item_input.send_keys("TestItem")
    
    add_item_button = driver.find_element_by_xpath('//button[text()="Add Item"]')
    add_item_button.click()

    driver.implicitly_wait(3)
    
    # Mark item as In Progress
    in_progress_item_button = driver.find_element_by_xpath('//button[text()="Mark as In-Progress"]')
    in_progress_item_button.click()
    
    # Complete item
    complete_item_button = driver.find_element_by_xpath('//button[text()="Mark as Completed"]')
    complete_item_button.click()

    # Delete item
    delete_item_button = driver.find_element_by_xpath('//button[text()="Delete"]')
    delete_item_button.click()