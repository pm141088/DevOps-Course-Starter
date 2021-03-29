from flask_login import UserMixin
from entity.role import Role

write_access = ['pm141088']

class User(UserMixin):
    def __init__(self, user_id):
        self.id = user_id
        self.user_id = user_id

    def get_id(self):
        return self.id
    
    def get_user_id(self):
        return self.user_id
    
    def get_role(self):
        return Role.Writer if self.user_id in write_access else Role.Reader