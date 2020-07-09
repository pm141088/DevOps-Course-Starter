from flask import Flask, render_template, request, redirect, url_for
import trello_items as trello

app = Flask(__name__)

@app.route('/') 
def index():
    items = sorted(trello.get_items(), key=lambda i: i.status, reverse=True)
    return render_template('index.html', items=items)

@app.route('/', methods=['POST'])
def add_item():
    title = request.form['item_title']
    description = request.form['item_description']
    trello.add_item(title, description)
    return redirect(url_for('index'))

@app.route('/items/<id>/complete', methods=['POST'])
def complete_item(id):
    trello.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/inprogress', methods=['POST'])
def in_progress_item(id):
    trello.in_progress_item(id)
    return redirect(url_for('index'))

@app.route('/items/<id>/uncomplete', methods=['POST'])
def uncomplete_item(id):
    trello.uncomplete_item(id)
    return redirect(url_for('index'))

@app.route('/items/delete/<id>', methods=['POST'])
def delete_item(id):
    trello.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
