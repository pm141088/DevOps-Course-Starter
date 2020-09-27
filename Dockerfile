# Docker images are layered, each command creates a new layer, by using the FROM directive you specify a base image upon which to build.
# Pull official python docker image
FROM python:3.8.5-slim-buster as base

# The command below will run at build time and installs poetry 
RUN pip install poetry

# The expose instruction infroms Docker that the container listens on teh specified network port at runtime
# Note the Expose instruction does not publish the port
EXPOSE 5000

# This is the active directory where commands will execute
WORKDIR /src
COPY . /src/

RUN poetry install --no-root --no-dev

FROM base as dev
ENV FLASK_ENV=development

ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0", "-p", "5000"] 

FROM base as prod
ENV FLASK_ENV=production

ENTRYPOINT ["poetry", "run", "gunicorn", "app:create_app()", "--bind", "0.0.0.0:80"]

