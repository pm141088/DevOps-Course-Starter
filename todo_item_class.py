from trello_config import Config
from enum import Enum
class Status(Enum):
    TO_DO = "To Do"
    DOING = "Doing"
    DONE = "Done"
class ToDoItem:
    def __init__(self, id, title, status, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    @classmethod
    def fromTrelloCard(cls, card, status):
        return cls(card['id'], card['name'], status, card['desc'])