#!/bin/bash

terraform init
terraform apply -var="client_id=$CLIENT_ID" -var="client_secret=$CLIENT_SECRET" -var="prefix=$ENV_PREFIX" -auto-approve
curl -dH -X POST "$(terraform output -raw webhook_url)"