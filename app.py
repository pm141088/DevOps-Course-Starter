from flask import Flask, render_template, request, redirect, url_for
import trello_items

app = Flask(__name__)

@app.route('/') 
def index():
    items = trello_items.get_items()
    sorted_items = sorted(items, key=lambda item: item['status'], reverse=True)
    return render_template('index.html', items=sorted_items)

@app.route('/', methods=['POST'])
def add_item():
    title = request.form['item_title']
    description = request.form['item_description']
    trello_items.add_item(title, description)
    return redirect(url_for('index'))

@app.route('/items/<int:id>', methods=['POST'])
def complete_item(id):
    trello_items.complete_item(id)
    return redirect(url_for('index'))

@app.route('/items/<int:id>', methods=['POST'])
def in_progress_item(id):
    trello_items.in_progress_item(id)
    return redirect(url_for('index'))

@app.route('/items/delete/<int:id>', methods=['POST'])
def delete_item(id):
    trello_items.delete_item(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
