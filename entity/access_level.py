from flask_login import current_user
from functools import wraps
from flask import abort, current_app
from entity.user import User
from entity.role import Role

import os
import logging
log = logging.getLogger('app')

'''
Just like decorators in Python allow us to add additional functionality to functions. View decorators in Flask allow us to add additional functionality to routes.
This will ensure that that the current user has write access before calling the actual function. If they do not a 403 error is raised.
'''

def restricted(func):
    @wraps(func)
    def decorated_view(*args, **kwargs):
        
        login_disabled = os.getenv('LOGIN_DISABLED') == 'True'

        user = User(current_user.get_id())
        if (login_disabled or user.get_role() == Role.Writer):
            log.debug(f'User "{current_user.get_id()}" is authorised and has write permissions')
            return func(*args, **kwargs)
        else:
            log.debug(f'User "{current_user.get_id()}" does not have write permissions')
            abort(403, "User is unauthorised to perform this action...")

    return decorated_view