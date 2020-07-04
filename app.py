from flask import Flask, render_template, request, redirect, url_for
import trello_items

app = Flask(__name__)

@app.route('/') 
def index():
    #items = trello_items.get_items()
    items = sorted(trello_items.get_items(), key=lambda i: i.status, reverse=True)
    return render_template('index.html', items=items)

@app.route('/', methods=['POST'])
def add_item():
    title = request.form['item_title']
    description = request.form['item_description']
    trello_items.add_item(title, description)
    return redirect(url_for('index'))

@app.route('/items/<id>/complete', methods=['POST'])
def complete_item(id):
    trello_items.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/uncomplete', methods=['POST'])
def uncomplete_item(id):
    trello_items.uncomplete_item(id)
    return redirect(url_for('index'))

@app.route('/items/delete/<id>', methods=['POST'])
def delete_item(id):
    trello_items.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
