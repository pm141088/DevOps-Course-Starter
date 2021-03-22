from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, login_required, login_user, current_user
from oauthlib.oauth2 import WebApplicationClient
import requests
import os
import sys
import logging

from view_model import ViewModel
from entity.user import User

from mongo_db.index import get_db_collection
from mongo_db.db_queries import get_all_items, mark_item_as_complete, mark_item_as_uncomplete, mark_item_as_in_progress, add_new_item, remove_item

date_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

def create_app():
    app = Flask(__name__)
    app.secret_key = os.environ.get("SECRET_KEY") or os.urandom(24)

    handler = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    collection = get_db_collection()

    # User session management setup
    login_manager = LoginManager()

    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET')

    authorization_url = 'https://github.com/login/oauth/authorize'
    access_token_url = 'https://github.com/login/oauth/access_token'
    
    # OAuth 2.0 Client setup
    oauth_client = WebApplicationClient(client_id)
    
    @login_manager.unauthorized_handler
    def unauthenticated():
        request_uri = oauth_client.prepare_request_uri(
            authorization_url
        )
        return redirect(request_uri)

    @login_manager.user_loader
    def load_user(user_id):
        return User(user_id)

    login_manager.init_app(app)

    @app.route('/') 
    @login_required
    def index():
        items = get_all_items(collection)
        return render_template('index.html', view_model=ViewModel(items))

    @app.route('/', methods=['POST'])
    @login_required
    def add_item():
        title = request.form['item_title']
        description = request.form['item_description']
        add_new_item(collection, title, description)
        return redirect(url_for('index'))

    @app.route('/items/<id>/complete', methods=['POST'])
    @login_required
    def complete_item(id):
        mark_item_as_complete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/inprogress', methods=['POST'])
    @login_required
    def in_progress_item(id):
        mark_item_as_in_progress(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/uncomplete', methods=['POST'])
    @login_required
    def uncomplete_item(id):
        mark_item_as_uncomplete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/delete/<id>', methods=['POST'])
    @login_required
    def delete_item(id):
        remove_item(collection, id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)

    return app