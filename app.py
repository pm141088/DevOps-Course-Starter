from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

# Index.html
@app.route('/') 
def index():
    items = session.get_items()
    sorted_items = sorted(items, key=lambda item: 0 if item['status'] == "Not Started" else 1)
    return render_template('index.html', items=sorted_items)

# Add an item
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == 'POST':
        req = request.form
        title = req['title']
        status = req['status']
        new_item = session.add_item(title, status)
        return redirect(url_for('index'))
    else:
        return render_template('add_item.html')

# Read an item by ID
@app.route('/read_item/<int:id>', methods=['GET'])
def read_item(id):
    found_item = session.get_item(id)
    return render_template('read_item.html', found_item=found_item)

# Delete an item by ID
@app.route('/read_item/<int:id>/delete', methods=['GET', 'DELETE'])
def delete_item(id):
    session.delete_item(id)
    return redirect(url_for('index'))

# Mark an item as 'In Progress'
@app.route('/read_item/<int:id>/status-in-progress', methods=['PUT', 'POST'])
def status_in_progress(id):
    item = session.get_item(id)
    if item != None:
        item['status'] = "In Progress"
        session.save_item(item)
        return redirect(url_for('index'))

# Mark an item as 'Completed'
@app.route('/read_item/<int:id>/status-completed', methods=['PUT', 'POST'])
def status_completed(id):
    item = session.get_item(id)
    if item != None:
        item['status'] = "Completed"
        session.save_item(item)
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run()
