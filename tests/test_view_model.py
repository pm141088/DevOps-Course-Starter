import pytest
from view_model import ViewModel
from entity.status import Status
from entity.item import Item
from datetime import datetime, timedelta

# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such input data. 
# Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
# To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py.

@pytest.fixture
def to_do_item():
    return Item('to-do-id', 'to-do-title', Status.TO_DO.value, 'to-do-description', "2021-01-01T15:47:23.517Z")

@pytest.fixture
def doing_item():
    return Item('doing-id', 'doing-title', Status.DOING.value,'doing-description', "2021-01-01T15:47:23.517Z")

@pytest.fixture
def done_item():
    return Item('done-id', 'done-title', Status.DONE.value, 'done-description', "2021-01-01T15:47:23.517Z")

@pytest.fixture
def view_model():
    return ViewModel(
        [
            Item('to-do-id', 'to-do-title', Status.TO_DO.value, 'to-do-description', "2021-01-01T15:47:23.517Z"),
            Item('doing-id', 'doing-title', Status.DOING.value, 'doing-description', "2021-01-01T15:47:23.517Z"),
            Item('done-id', 'done-title', Status.DONE.value, 'done-description', "2021-01-01T15:47:23.517Z")
        ]
    )

@pytest.fixture
def done_items_view_model():
    return ViewModel(
        [
            Item('to-do-id', 'to-do-title', Status.DONE.value, '5 days done', datetime.now() - timedelta(days=5)),
            Item('to-do-id', 'to-do-title', Status.DONE.value, '3 hours done', datetime.now() - timedelta(hours=3)),
            Item('to-do-id', 'to-do-title', Status.DONE.value, 'Just done', datetime.now()),
            Item('to-do-id', 'to-do-title', Status.DONE.value, '20 days done', datetime.now() - timedelta(days=20)),
            Item('to-do-id', 'to-do-title', Status.DONE.value, '20 hours done', datetime.now() - timedelta(hours=20))
        ]
    )

# A test function can use a fixture by mentioning the fixture name as an input parameter.
def test_return_all_items(view_model):
    all_items = view_model.all_items
    assert len(all_items) == 3

def test_return_to_do_items(view_model):
    to_do_items = view_model.to_do_items
    assert len(to_do_items) == 1
    assert to_do_items[0].title == 'to-do-title'
    
def test_return_doing_items(view_model):
    doing_items = view_model.doing_items
    assert len(doing_items) == 1
    assert doing_items[0].title == 'doing-title'

def test_return_done_items(view_model):
    done_items = view_model.done_items
    assert len(done_items) == 1
    assert done_items[0].title == 'done-title'

def test_show_all_done_items_true(view_model):
    assert view_model.show_all_done_items is True

def test_show_all_done_items_false(done_items_view_model):
    assert done_items_view_model.show_all_done_items is False

def test_return_recent_done_items(done_items_view_model):
    recent_done_items = done_items_view_model.recent_done_items
    assert len(recent_done_items) == 3

def test_return_older_done_items(done_items_view_model):
    older_done_items = done_items_view_model.older_done_items
    assert len(older_done_items) == 2