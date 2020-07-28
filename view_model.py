from todo_item_class import Status
from datetime import datetime

def _today():
    return datetime.date(datetime.today())

class ViewModel:
    def __init__(self, items):
        self._items = items

    @property
    def items(self):
        return self._items

    @property
    def to_do_items(self):
        # Python list comprehension [expression for item in list]
        return [item for item in self._items if item.status == Status.TO_DO]

    @property
    def doing_items(self):
        return [item for item in self._items if item.status == Status.DOING]

    @property
    def done_items(self):
        return [item for item in self._items if item.status == Status.DONE]
    
    @property
    def show_all_done_items(self):
        return len(self.done_items) < 5
    
    @property
    def recent_done_items(self):
        return [item for item in self.done_items if datetime.date(item.last_modified) == _today()]

    @property
    def older_done_items(self):
        return [item for item in self.done_items if datetime.date(item.last_modified) < _today()]