from bson.objectid import ObjectId
from datetime import datetime

from entity.status import Status
from entity.item import Item
import logging

date_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"
log = logging.getLogger('app')

def get_all_items(collection):
    """
        Fetches all to do list items from the db collection.
        Returns:
            list: The list of items.
    """
    log.debug(f'Function to return all items from the db collection has been invoked')
    items = [] # Append data to a list, then return it after the end of the loop
    for item in collection.find(): # The find() method returns all occurrences in the selection
        items.append(
            Item(
                item['_id'],
                item['title'],
                item['status'],
                item['description'],
                item['dateLastActivity']
            )
        )
    log.debug(f'{len(items)} items found in database')
    return items


def mark_item_as_complete(collection, id):
    """
        Moves an item from the In Progress list to Done list.
        Args:
            id: The id of the item to mark as to do.
    """
    log.debug(f'Request to mark item with id: {id} as complete')
    collection.update_one( #You can update a record, or document as it is called in MongoDB, by using the update_one() method
        {"_id": ObjectId(id)},
        {
            "$set": {
                "status": Status.DONE.value,
                "dateLastActivity":  datetime.now().strftime(date_time_format)
            }
        }
    )

def mark_item_as_uncomplete(collection, id):
    """
        Moves an item back to the to do list.
        Args:
            id: The id of the item to mark as to do.
    """
    log.debug(f'Request to mark item with id: {id} as uncompleted')
    collection.update_one( #You can update a record, or document as it is called in MongoDB, by using the update_one() method
        {"_id": ObjectId(id)},
        {
            "$set": {
                "status": Status.TO_DO.value,
                "dateLastActivity":  datetime.now().strftime(date_time_format)
            }
        }
    )


def mark_item_as_in_progress(collection, id):
    """
        Moves an item from the To Do list to In Progress list.
        Args:
            id: The id of the item to mark as in progress.
    """
    log.debug(f'Request to mark item with id: {id} as in progress')
    collection.update_one( #You can update a record, or document as it is called in MongoDB, by using the update_one() method
        {"_id": ObjectId(id)},
        {
            "$set": {
                "status": Status.DOING.value,
                "dateLastActivity":  datetime.now().strftime(date_time_format)
            }
        }
    )


def add_new_item(collection, title, description):
    """
        Adds a new item with the specified title and description to the db collection.
        Args:
            title: The title of the item.
            description: The description of the item.
    """
    log.debug(f'Request to add a new item with title: {title} and description: {description}')
    collection.insert_one(
        {
            "title": title,
            "status": Status.TO_DO.value,
            "description": description,
            "dateLastActivity": datetime.now().strftime(date_time_format)
        }
    )


def remove_item(collection, id):
    """
        Removes an existing item from the collection. 
        Args:
            id: The id of the item to remove.
    """
    log.debug(f'Request to delete item with id: {id}')
    collection.delete_one(
        {
            "_id": ObjectId(id)
        }
    )