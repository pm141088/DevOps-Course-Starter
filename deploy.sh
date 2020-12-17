#!/bin/bash

# Get the latest image from Docker Hub (built by your CI pipeline)
docker pull pm141088/todo-app:latest
# Tag it for Heroku
docker tag pm141088/todo-app registry.heroku.com/pm141088-todo-app/web
# Push it to Heroku registry
docker push registry.heroku.com/pm141088-todo-app/web
# Release the image to your app
heroku container:release web --app pm141088-todo-app