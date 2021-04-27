from entity.status import Status
from datetime import datetime, timedelta

class ViewModel:
    def __init__(self, items, reader):
        self._items = items
        self._reader = reader

    @property
    def all_items(self):
        return self._items

    @property
    def to_do_items(self):
        # Python list comprehension [expression for item in list]
        return [item for item in self._items if item.status == Status.TO_DO.value]

    @property
    def doing_items(self):
        return [item for item in self._items if item.status == Status.DOING.value]

    @property
    def done_items(self):
        return [item for item in self._items if item.status == Status.DONE.value]
    
    @property
    def show_all_done_items(self):
        return len(self.done_items) < 5
    
    @property
    def recent_done_items(self):
        return [item for item in self.done_items if datetime.now() - timedelta(days=1) < item.last_modified]

    @property
    def older_done_items(self):
        return list(set(self.done_items) - set(self.recent_done_items))
    
    @property
    def reader(self):
        return self._reader