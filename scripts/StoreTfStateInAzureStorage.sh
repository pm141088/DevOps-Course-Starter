#!/bin/bash

RESOURCE_GROUP_NAME="CreditSuisse1_PatrickMorris_ProjectExercise"
STORAGE_ACCOUNT_NAME="tstatesan"
CONTAINER_NAME="tstatecn"

# Create storage account
az storage account create --resource-group $RESOURCE_GROUP_NAME --name $STORAGE_ACCOUNT_NAME --sku Standard_LRS --encryption-services blob

# Get storage account key
ARM_ACCESS_KEY=$(az storage account keys list --resource-group $RESOURCE_GROUP_NAME --account-name $STORAGE_ACCOUNT_NAME --query '[0].value' -o tsv)

# Create blob container
az storage container create --name $CONTAINER_NAME --account-name $STORAGE_ACCOUNT_NAME --account-key $ARM_ACCESS_KEY

echo "ARM_ACCESS_KEY: $ARM_ACCESS_KEY"