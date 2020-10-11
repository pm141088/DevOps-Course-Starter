# DevOps Apprenticeship: Project Exercise

## System Requirements

The project uses Poetry for Python to created an isolated environment and manage package depencies. Poetry is a tool for dependency management and packaging in Python.

You will need to have an official distribution of Python version ^3.7. Follow instructions on this page to install poetry: (https://python-poetry.org/docs/#system-requirements)

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```
## Dependencies

This project uses a virtual environment to isolate package dependenceis. To create a virtual environment and install required packages, run the following from a shell prompt:

```bash
$ poetry install
```

You'll also need to clone a new `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change).

## Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
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

### Connecting to Trello

To run the app with a Trello board, copy the contents of `env.template` into an `.env` file. 
Copy and paste your Trello API key and token from (https://trello.com/app-key) into the respective values.
You will also need to enter Trello board ID, to do list ID, doing list id and done list id.

## Running the App in a VM

### Vagrant

You can run this on a VM by running `vagrant up` at the root. Once the command has finished, as above you can visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app. Any logs from this are saved to `applogs.txt`.

### Docker

During first time setup, run the following commands:

Dev:
To run the app on Docker in development mode (with hot reloading), run `docker-compose up --build dev-app`

Prod:
To run the app on Docker in production mode, run `docker-compose up --build prod-app`. 

In subsequent runs you can omit the `--build` flag. Once again the app can then be found at [`http://localhost:5000/`]

## Testing

### Prerequisites to run e2e test using Selenium ###

You will need a `Chromedriver.exe` in order to run e2e tests, please add this to the drivers folder upon checkout.
Line #31 in the test_app_e2e.py file will need to be updated with the path to the Chromedriver.

### Running the tests
To run all tests, run `pytest`
To run integration tests, run `pytest test_app.py`
To run end-to-end tests, run `pytest test_app_e2e.py`