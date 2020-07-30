import pytest
from view_model import ViewModel
from todo_item_class import ToDoItem, Status
from datetime import datetime, timedelta

# Fixtures are functions, which will run before each test function to which it is applied.
# Fixtures are used to feed some data to the tests such input data. 
# Therefore, instead of running the same code for every test, we can attach fixture function to the tests and it will run and return the data to the test before executing each test.
# To make a fixture available to multiple test files, we have to define the fixture function in a file called conftest.py.

@pytest.fixture
def items_view_model():
    return ViewModel([
        ToDoItem(1, "Title 1", Status.TO_DO, "Desc #1", datetime.now()),
        ToDoItem(2, "Title 2", Status.TO_DO, "Desc #2", datetime.now()),
        ToDoItem(3, "Title 3", Status.DOING, "Desc #3", datetime.now()),
        ToDoItem(4, "Title 4", Status.DONE, "Desc #4", datetime.now()),
        ToDoItem(5, "Title 5", Status.DONE, "Desc #5", datetime.now()),
    ])

@pytest.fixture
def done_items_view_model():
    return ViewModel([
        ToDoItem(6, "Title 1", Status.DONE, "5 days done", datetime.now() - timedelta(days=5)),
        ToDoItem(7, "Title 2", Status.DONE, "3 hours done", datetime.now() - timedelta(hours=3)),
        ToDoItem(8, "Title 3", Status.DONE, "Just done", datetime.now()),
        ToDoItem(9, "Title 4", Status.DONE, "20 days done", datetime.now() - timedelta(days=20)),
        ToDoItem(10, "Title 5", Status.DONE, "20 hours done", datetime.now() - timedelta(hours=20))
    ])

# A test function can use a fixture by mentioning the fixture name as an input parameter.
def test_return_all_items(items_view_model):
    all_items = items_view_model.items
    assert len(all_items) == 5
    assert all_items[0].id == 1

def test_return_to_do_items(items_view_model):
    to_do_items = items_view_model.to_do_items
    assert len(to_do_items) == 2
    assert to_do_items[0].id == 1
    assert to_do_items[1].id == 2

def test_return_doing_items(items_view_model):
    doing_items = items_view_model.doing_items
    assert len(doing_items) == 1
    assert doing_items[0].id == 3

def test_return_done_items(items_view_model):
    done_items = items_view_model.done_items
    assert len(done_items) == 2
    assert done_items[0].id == 4

def test_show_all_done_items_true(items_view_model):
    assert items_view_model.show_all_done_items is True

def test_show_all_done_items_false(done_items_view_model):
    assert done_items_view_model.show_all_done_items is False

def test_return_recent_done_items(done_items_view_model):
    recent_done_items = done_items_view_model.recent_done_items
    assert len(recent_done_items) == 3
    assert set([item.id for item in recent_done_items]) == set([7, 8, 10])

def test_return_older_done_items(done_items_view_model):
    older_done_items = done_items_view_model.older_done_items
    assert len(older_done_items) == 2    
    assert set([item.id for item in older_done_items]) == set([6, 9])