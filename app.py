from flask import Flask, render_template, request, redirect, url_for
import session_items as session
from flask_modus import Modus

app = Flask(__name__)
modus = Modus(app)
app.config.from_object('flask_config.Config')

# Index.html
@app.route('/') #localhost
def index():
    return render_template('index.html', get_items=session.get_items())

# Add an item
@app.route('/add_item', methods=['GET', 'POST'])
def add_item():

    if request.method == 'POST':

        req = request.form

        new_item = req['title']

        print(new_item)

        session.add_item(new_item)

        return redirect('/')

    return render_template('add_item.html')

@app.route('/read_item/<int:id>', methods=['GET', 'PATCH', 'DELETE'])
def read_item(id):
    found_item = session.get_item(id)
    get_items = session.get_items()
    if request.method == b'PATCH':
        #found_item.status = request.form['status']
        #found_item.title = request.form['title']
        return redirect(url_for('index'))
    if request.method == b'DELETE':
        session.delete_item(id)
        return redirect(url_for('index'))
    return render_template('read_item.html', found_item=found_item)

# Edit an item
@app.route('/read_item/<int:id>/edit')
def edit_item(id):

    found_item = session.get_item(id)
    print(found_item)

    return render_template('edit_item.html', found_item=found_item)

if __name__ == '__main__':
    app.run()
