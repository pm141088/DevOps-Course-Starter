from trello_config import Config
from todo_item_class import ToDoItem, Status
import requests

class Trello:
    def __init__(self, dotenv):
        self.config = Config(dotenv)
        self.trello_web_url = 'https://api.trello.com/1'
        self.trello_board_url = f'{self.trello_web_url}/boards/{self.config.board_id}/cards'
        self.trello_cards_url = f'{self.trello_web_url}/cards'
        self.trello_auth = { 'key': self.config.api_key, 'token': self.config.api_token }

    def get_trello_card_url(self, id):
        return f'{self.trello_cards_url}/{id}'

    def get_status(self, list_id):
        if list_id == self.config.todo_list_id:
            return Status.TO_DO
        elif list_id == self.config.doing_list_id:
            return Status.DOING
        else:
            return Status.DONE

    def get_items(self):
        """
        Fetches all to do items from Trello.

        Returns:
            list: The list of saved items.
        """
        api_method = 'GET'
        response = requests.request(api_method, self.trello_board_url, params=self.trello_auth).json()
        
        return [ToDoItem.fromTrelloCard(card, self.get_status(card['idList'])) for card in response]

    def add_item(self, title, description = ''):
        """
        Adds a new item with the specified title & description to Trello. 

        Args:
            title: The title of the item.
            description: The description of the item

        Returns:
            item: The saved item.
        """
        api_method = 'POST'
        requests.request(api_method, self.trello_cards_url, params={**self.trello_auth, 'idList': self.config.todo_list_id, 'name': title, 'desc': description })

    def complete_item(self, id):
        """
        Moves a Trello item card from the To Do list to Done.

        Args:
            id: The id of the item to mark as complete.
        """
        api_method = 'PUT'
        requests.request(api_method, self.get_trello_card_url(id), params={**self.trello_auth, 'idList': self.config.done_list_id })

    def in_progress_item(self, id):
        """
        Moves a Trello item card from the To Do list to Doing list.

        Args:
            id: The id of the item to mark as complete.
        """
        api_method = 'PUT'
        requests.request(api_method, self.get_trello_card_url(id), params={**self.trello_auth, 'idList': self.doing_list_id })

    def uncomplete_item(self, id):
        """
        Moves an item with specified ID to the To Do list in Trello.

        Args:
            id: the ID of the item
        """
        api_method = 'PUT'
        requests.request(api_method, self.get_trello_card_url(id), params={**self.trello_auth, 'idList': self.todo_list_id })

    def delete_item(self, id):
        """
        Removes an existing item from Trello. 

        Args:
            id: The id of the item to remove.
        """
        api_method = 'DELETE'
        requests.request(api_method, self.get_trello_card_url(id), params=self.trello_auth)

    def create_trello_board(self, name):
        """
        Creates a new Trello board.

        Args:
            name: The name of the new board to create.
        """
        response = requests.request('POST', f'{self.trello_web_url}/boards', params={**self.trello_auth, 'name': name }).json()
        return response['id']

    def delete_trello_board(self, id):
        """
        Removes an existing board from Trello.

        Args:
            id: The id of the board to remove.
        """
        requests.request('DELETE', f'{self.trello_web_url}/boards/{id}', params=self.trello_auth)