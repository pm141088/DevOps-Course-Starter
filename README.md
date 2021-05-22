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

## OAuth 2.0 Setup

Navigate to https://github.com/settings/applications/new and fill in the form. (Make sure you're logged into your github account!)

1. Name the application e.g. DevOps ToDo App (Local)
2. Set HomePage URL to: "http://localhost:5000/"
3. Set Authorization callback URL to: "http://localhost:5000/login/callback"
4. Copy the "Client ID" and set the CLIENT_ID to this value in the .env file
5. Click on "Generate a new client secret", copy the secret and set the CLIENT_SECRET to this value in the .env file

To application runs with OAuth by default, to disable set `LOGIN_DISABLED=True` in your `.env` file.

There are two authorisation roles:
• reader - These users can view to-dos but not change or create new ones
• writer - These users can also change existing to-dos or create new ones
By default all users will have Read Only permmissions on the app unless the user is added to the hardcoded list `writer_access` in `user.py`. 

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

### MongoDB Setup / Configuration

This application is configured to use a MongoDB cluster which was created using the 'free to use' MongoDB Atlas service. When creating the cluster, please select the 'username and password' authentication method and make sure you add your local IP address when prompted (there's a button to do this automatically) so you can access the cluster from your local machine.

To run the app with MongoDB, copy the contents of `env.template` into an `.env` file and update the relvant environment variables.
You will also need to update the MongoDB cluster name found in dbClientUri on index.py 

## Running the App in a VM

### Vagrant

You can run this on a VM by running `vagrant up` at the root. Once the command has finished, as above you can visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app. Any logs from this are saved to `applogs.txt`.

### Docker

During first time setup, run the following commands:

Dev:
To run the app on Docker in development mode (with hot reloading), run `docker-compose up --build dev-app`

Prod:
To run the app on Docker in production mode, run `docker-compose up --build prod-app`. 

In subsequent runs you can omit the `--build` flag. Once again the app can then be found at [`http://localhost:8080/`]

## Testing

### Prerequisites

You will need a `Chromedriver.exe` file at the project root and Chrome installed. 

### Running the tests
To run all tests, run `pytest`.
To run unit tests, run `pytest tests`.
To run integration tests, run `pytest tests_integration`.
To run end-to-end tests, run `pytest tests_e2e`.

### Running the tests in a Docker container 

To run the tests in a Docker container, run  `docker build --target test --tag test .` to build the container and
 * `docker run test tests` to run all the unit tests.
 * `docker run test tests_integration` to run all the integration tests.
 * `docker run --env-file .env test tests_e2e` to run all the end-to-end tests.
 * `docker run --env-file .env test` to run all the tests.

### Documentation

A collection of C4 model Architecture diagrams have been created to visualise the hierachy of abstractions in the application. These include a Context, Container, and Component diagram. These can be viewed at `https://app.diagram.net`.

## Cloud Infrastructure as Code (IaC)

This web application is hosted on Azure. The underlying infrastructure has been created using Terraform, an open source "IaC" tool which allows us to use declaritve coding to desribe the desired "end-state" infrastructure for running an applcation.

## Basic Concept of Terraform Workflow
To make any changes to the infrastructure, you should edit the terraform files and then apply the changes. Avoid making changes directly on the Azure portal.

The workflows of Terraform are built on top of five key steps: Write, Init, Plan, Apply, and Destroy. See below for details:

1. Run `terraform init` - This command is used to initialize the working directory containing Terraform configuration files. It is safe to run this command multiple times.
2. Make changes to your Terraform code.
3. Create an execution plan using `terraform plan` command, this is a handy way to check whether the execution plan matches your expectations without making any changes to real resources or to the state.
4. Apply your changes by runing the `terraform apply` command. Terraform apply command is used to create or introduce changes to real infrastructure.
5. To destroy infrastructure governed by terraform you can you run `terraform destroy` command. 

### State storage

This application uses Azure Blob storage to store remote state. The setup for this was done by running: `\scripts\StoreTfStateInAzureStorage.sh`. There is no need to execute this script again unless the state needs ot be setup again. 