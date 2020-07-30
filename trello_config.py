"""Trello configuration class."""
import os
from dotenv import find_dotenv, load_dotenv

class Config:
    """Base configuration variables."""
    def __init__(self, dotenv):
        file_path = find_dotenv(dotenv)
        load_dotenv(file_path, override=True)

        API_KEY = os.environ.get('TRELLO_API_KEY')
        API_TOKEN = os.environ.get('TRELLO_API_TOKEN')

        if dotenv == '.env' and (not (API_KEY and API_TOKEN)):
            raise ValueError("No Trello credentials set for Flask application. Did you forget to run setup.sh?")

        self.api_key = API_KEY
        self.api_token = API_TOKEN
        self.board_id = os.environ.get('TRELLO_BOARD_ID')
        self.todo_list_id = os.environ.get('TRELLO_TODO_LIST_ID')
        self.doing_list_id = os.environ.get('TRELLO_DOING_LIST_ID')
        self.done_list_id = os.environ.get('TRELLO_DONE_LIST_ID')