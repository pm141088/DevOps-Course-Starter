from flask import Flask, render_template, request, redirect, url_for
import session_items as session

app = Flask(__name__)
app.config.from_object('flask_config.Config')

@app.route('/')
def index():
    return render_template('index.html', get_items=session.get_items())

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():

    if request.method == 'POST':

        req = request.form

        item = req["title"]

        print(item)

        session.add_item(item)

        return redirect('/')



    return render_template('add_item.html')

if __name__ == '__main__':
    app.run()
