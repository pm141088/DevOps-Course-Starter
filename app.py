from flask import Flask, render_template, request, redirect, url_for
""" Flask-Login 
Flask-Login provides user session management for Flask. It handles the common tasks of logging in, logging out, and remembering your users’ sessions over extended periods of time.
https://flask-login.readthedocs.io/en/latest/
"""
from flask_login import LoginManager, login_required, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient
import requests
import os
import sys
import logging

from view_model import ViewModel
from entity.user import User
from entity.role import Role
from entity.access_level import restricted
from mongo_db.index import get_db_collection
from mongo_db.db_queries import get_all_items, mark_item_as_complete, mark_item_as_uncomplete, mark_item_as_in_progress, add_new_item, remove_item

date_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    #login_disabled = os.getenv('LOGIN_DISABLED') == 'False'
    #app.config['LOGIN_DISABLED'] = login_disabled

    def is_login_disabled():
        if('LOGIN_DISABLED' in app.config):
            return app.config['LOGIN_DISABLED']
        return False

    handler = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    collection = get_db_collection()

    # User session management setup
    login_manager = LoginManager()

    # This information is obtained upon registration of a new GitHub account
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')
    authorization_url = 'https://github.com/login/oauth/authorize'
    access_token_url = 'https://github.com/login/oauth/access_token'
    
    # OAuth 2.0 Client setup
    oauth_client = WebApplicationClient(client_id)
    
    # Logic to redirect to Github OAuth flow when unauthenticated
    @login_manager.unauthorized_handler
    def unauthenticated():
        request_uri = oauth_client.prepare_request_uri(authorization_url)
        return redirect(request_uri)

    # This callback is used to reload the user object from the user ID stored in the session.
    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    # Once the actual application object has been created, you can configure it for login with: 
    login_manager.init_app(app)

    # Implement the callback route
    @app.route("/login/callback", methods=["GET"])
    def callback():
        token_url, token_headers, token_body = oauth_client.prepare_token_request(
            token_url="https://github.com/login/oauth/access_token",
            authorization_response=request.url,
            client_secret=client_secret
        )
        token_response = requests.post(
            token_url,
            headers=token_headers,
            data=token_body
        )
        oauth_client.parse_request_body_response(
            token_response.content.decode()
        )

        # Add token to the request uri, body or authorization header.
        user_info_request_url, user_info_request_headers, user_info_request_body = oauth_client.add_token(
            uri='https://api.github.com/user',
        )
        user_info_response = requests.get(
            user_info_request_url,
            data=user_info_request_body,
            headers=user_info_request_headers
        )

        github_username = user_info_response.json()['login']
        user = User(github_username)
        login_success = login_user(user)

        if login_success:
            return redirect(url_for('index'))

    @app.route('/') 
    @login_required
    def index():
        #reader = User(current_user.get_role()) == Role.Reader
        reader = None

        items = get_all_items(collection)
        return render_template('index.html', view_model=ViewModel(items, reader), login_disabled=is_login_disabled(), current_user=current_user)

    @app.route('/', methods=['POST'])
    @login_required
    @restricted
    def add_item(): 
        title = request.form['item_title']
        description = request.form['item_description']
        add_new_item(collection, title, description)
        return redirect(url_for('index'))
        
    @app.route('/items/<id>/complete', methods=['POST'])
    @login_required
    @restricted
    def complete_item(id):
        mark_item_as_complete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/inprogress', methods=['POST'])
    @login_required
    @restricted
    def in_progress_item(id):
        mark_item_as_in_progress(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/uncomplete', methods=['POST'])
    @login_required
    @restricted
    def uncomplete_item(id):
        mark_item_as_uncomplete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/delete/<id>', methods=['POST'])
    @login_required
    @restricted
    def delete_item(id):
        remove_item(collection, id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)

    return app