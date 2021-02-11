from flask import Flask, render_template, request, redirect, url_for
import sys
import logging 
#from trello_items import Trello
from view_model import ViewModel

from mongo_db.index import get_db_collection
from mongo_db.db_queries import get_all_items, mark_item_as_complete, mark_item_as_uncomplete, mark_item_as_in_progress, add_new_item, remove_item

date_time_format = "%Y-%m-%dT%H:%M:%S.%fZ"

def create_app():
    app = Flask(__name__)
    #trello = Trello(dotenv)

    handler = logging.StreamHandler(sys.stdout)
    app.logger.addHandler(handler)
    app.logger.setLevel(logging.DEBUG)

    collection = get_db_collection()

    @app.route('/') 
    def index():
        items = get_all_items(collection)
        return render_template('index.html', view_model=ViewModel(items))

    @app.route('/', methods=['POST'])
    def add_item():
        title = request.form['item_title']
        description = request.form['item_description']
        add_new_item(collection, title, description)
        return redirect(url_for('index'))

    @app.route('/items/<id>/complete', methods=['POST'])
    def complete_item(id):
        mark_item_as_complete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/inprogress', methods=['POST'])
    def in_progress_item(id):
        mark_item_as_in_progress(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/<id>/uncomplete', methods=['POST'])
    def uncomplete_item(id):
        mark_item_as_uncomplete(collection, id)
        return redirect(url_for('index'))

    @app.route('/items/delete/<id>', methods=['POST'])
    def delete_item(id):
        remove_item(collection, id)
        return redirect(url_for('index'))

    if __name__ == '__main__':
        app.run(debug=True)

    return app