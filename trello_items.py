from trello_config import Config
from todo_item_class import ToDoItem, Status
import requests

config = Config('.env')

trello_board_url = f'https://api.trello.com/1/boards/{config.board_id}/cards'
trello_cards_url = 'https://api.trello.com/1/cards'
trello_auth = { 'key': config.api_key, 'token': config.api_token }

def get_trello_card_url(id):
    return f'{trello_cards_url}/{id}'

def get_status(list_id):
    if list_id == config.todo_list_id:
        return Status.TO_DO
    elif list_id == config.doing_list_id:
        return Status.DOING
    else:
        return Status.DONE

def get_items():
    """
    Fetches all to do items from Trello.

    Returns:
        list: The list of saved items.
    """
    api_method = 'GET'
    response = requests.request(api_method, trello_board_url, params=trello_auth).json()
    #print(response.text)
    
    return [ToDoItem.fromTrelloCard(card, get_status(card['idList'])) for card in response]

def add_item(title, description = ''):
    """
    Adds a new item with the specified title & description to Trello. 

    Args:
        title: The title of the item.
        description: The description of the item

    Returns:
        item: The saved item.
    """
    api_method = 'POST'
    requests.request(api_method, trello_cards_url, params={**trello_auth, 'idList': config.todo_list_id, 'name': title, 'desc': description })

def complete_item(id):
    """
    Moves a Trello item card from the To Do list to Done.

    Args:
        id: The id of the item to mark as complete.
    """
    api_method = 'PUT'
    requests.request(api_method, get_trello_card_url(id), params={**trello_auth, 'idList': config.done_list_id })

def in_progress_item(id):
    """
    Moves a Trello item card from the To Do list to Doing list.

    Args:
        id: The id of the item to mark as complete.
    """
    api_method = 'PUT'
    requests.request(api_method, get_trello_card_url(id), params={**trello_auth, 'idList': doing_list_id })

def uncomplete_item(id):
    """
    Moves an item with specified ID to the To Do list in Trello.

    Args:
        id: the ID of the item
    """
    api_method = 'PUT'
    requests.request(api_method, get_trello_card_url(id), params={**trello_auth, 'idList': todo_list_id })

def delete_item(id):
    """
    Removes an existing item from Trello. 

    Args:
        id: The id of the item to remove.
    """
    api_method = 'DELETE'
    requests.request(api_method, get_trello_card_url(id), params=trello_auth)