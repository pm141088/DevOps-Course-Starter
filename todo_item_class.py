class ToDoItem:
    def __init__(self, id, title, status, description):
        self.id = id
        self.title = title
        self.status = status
        self.description = description

    @classmethod
    def fromTrelloCard(cls, card, idList):
        status = 'Not Started' if card['idList'] == idList else 'Completed'
        return cls(card['id'], card['name'], status, card['desc'])