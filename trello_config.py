"""Trello configuration class."""
import os

class Config:
    """Base configuration variables."""
    TRELLO_API_KEY = os.environ.get('TRELLO_API_KEY')
    TRELLO_API_TOKEN = os.environ.get('TRELLO_API_TOKEN')
    TRELLO_BOARD_ID = os.environ.get('TRELLO_BOARD_ID')
    TRELLO_TODO_LIST_ID = os.environ.get('TRELLO_TODO_LIST_ID')
    TRELLO_DOING_LIST_ID = os.environ.get('TRELLO_DONE_LIST_ID')
    TRELLO_DONE_LIST_ID = os.environ.get('TRELLO_DONE_LIST_ID')

    if not (TRELLO_API_KEY and TRELLO_API_TOKEN):
        raise ValueError("No Trello credentials set for Flask application. Did you forget to run setup.sh?")

    if not (TRELLO_BOARD_ID and TRELLO_TODO_LIST_ID and TRELLO_DOING_LIST_ID and TRELLO_DONE_LIST_ID):
        raise ValueError("No Trello ID's set for flask application. Did you forget to run setup.sh?")