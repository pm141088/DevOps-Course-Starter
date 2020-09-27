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

### Running tests

To run all unit and integration tests, run `pytest` from terminal.

Alternatively, you can run specific tests by pointing 
pytest to a folder e.g. `pytest tests`.

### Instructions to run e2e test using Selenium ###
Chromedriver.exe is necessary for the e2e tests to run, please add this to the drivers folder upon checkout.
Line #31 in the test_app_e2e.py file will need to be updated with the path to the Chromedriver.