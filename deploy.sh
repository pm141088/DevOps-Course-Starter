#!/bin/bash

# Push it to Heroku registry
docker push registry.heroku.com/$HEROKU_APP/web
# Release the image to your app
heroku container:release web --app $HEROKU_APP