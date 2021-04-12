# Docker images are layered, each command creates a new layer, by using the FROM directive you specify a base image upon which to build.
# Pull official python docker image
FROM python:3.8.5-buster as base
RUN pip install "poetry==1.0.9"

# This is the active directory where commands will execute
COPY . /src/
WORKDIR /src
RUN poetry config virtualenvs.create false --local && \
  poetry install

# Production Stage
FROM base as production
CMD poetry run gunicorn --bind 0.0.0.0:${PORT} wsgi:app

# Development Stage
FROM base as development
RUN pip install poetry
RUN poetry install
EXPOSE 5000
ENTRYPOINT ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]

# Testing Stage
FROM base as test
RUN pip install poetry
RUN poetry install
COPY . /src/

# Install Chrome
RUN apt-get update &&\
  apt-get upgrade -y &&\
  curl -sSL https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb -o chrome.deb &&\
  apt-get install ./chrome.deb -y &&\
  rm ./chrome.deb

# Install Chromium WebDriver
RUN LATEST=`curl -sSL https://chromedriver.storage.googleapis.com/LATEST_RELEASE` &&\
 echo "Installing chromium webdriver version ${LATEST}" &&\
 curl -sSL https://chromedriver.storage.googleapis.com/${LATEST}/chromedriver_linux64.zip -o chromedriver_linux64.zip &&\
 apt-get install unzip -y &&\
 unzip ./chromedriver_linux64.zip

ENTRYPOINT [ "poetry", "run", "pytest" ]