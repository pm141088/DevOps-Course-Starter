# Azure Provider source and version being used
terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = ">=2.49"
    }
  }
}

# Configure the Microsoft Azure Provider
provider "azurerm" {
  features {}
}

# Create a resource group
data "azurerm_resource_group" "main" {
  name = "CreditSuisse1_PatrickMorris_ProjectExercise"
}

resource "azurerm_app_service_plan" "main" {
  name = "terraformed-asp"
  location = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  kind = "Linux"
  reserved = true
  
  sku {
    tier = "Basic"
    size = "B1"
  }
}

resource "azurerm_app_service" "main" {
  name = "terraform-todoapp-test"
  location = data.azurerm_resource_group.main.location
  resource_group_name = data.azurerm_resource_group.main.name
  app_service_plan_id = azurerm_app_service_plan.main.id
  
  site_config {
  app_command_line = ""
  linux_fx_version = "DOCKER|appsvcsample/python-helloworld:latest"
  }

  app_settings = {
  "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
  }
}
