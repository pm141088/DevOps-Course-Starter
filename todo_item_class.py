from trello_config import Config
class ToDoItem:
    def __init__(self, id, title, status, description):
        self.id = id
        self.title = title
        self.description = description
        self.status = status

    @classmethod
    def fromTrelloCard(cls, card, idList):
        status = ''
        if card['idList'] == Config.TRELLO_TODO_LIST_ID:
            status = 'Not Started'
        if card['idList'] == Config.TRELLO_DOING_LIST_ID:
            status = 'In Progress'
        if card['idList'] == Config.TRELLO_DONE_LIST_ID:
            status = 'Completed'  
        return cls(card['id'], card['name'], status, card['desc'])