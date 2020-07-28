from trello_config import Config
from dateutil import parser
from enum import Enum

class Status(Enum):
    TO_DO = "To Do"
    DOING = "Doing"
    DONE = "Done"
class ToDoItem:
    def __init__(self, id, title, status, description, last_modified):
        self.id = id
        self.title = title
        self.status = status
        self.description = description
        self.last_modified = parser.isoparse(last_modified).replace(tzinfo=None)

    @classmethod
    def fromTrelloCard(cls, card, status):
        return cls(card['id'], card['name'], status, card['desc'], card['dateLastActivity'])