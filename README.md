# DevOps Apprenticeship: Project Exercise

## Getting started

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from a bash shell terminal:

### On macOS and Linux
```bash
$ source setup.sh
```
### On Windows (Using Git Bash)
```bash
$ source setup.sh --windows
```

Once the setup script has completed and all packages have been installed, start the Flask app by running:
```bash
$ flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

### Instructions to run tests

To run all unit and integration tests, run `pytest` from terminal.

Alternatively, you can run specific tests by pointing 
pytest to a folder e.g. `pytest tests`.

### Connecting to Trello

To run the app with a Trello board, copy the contents of `env.test` into an `.env` file. 
Copy and paste your Trello API key and token from (https://trello.com/app-key) into the respective values.
You will also need to enter in the Trello board ID, to do list ID, doing list id and done list id.
TRELLO_API_KEY=
TRELLO_API_TOKEN=
TRELLO_BOARD_ID=
TRELLO_TODO_LIST_ID=
TRELLO_DOING_LIST_ID=
TRELLO_DONE_LIST_ID=