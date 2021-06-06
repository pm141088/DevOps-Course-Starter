variable "prefix" {
  description = "The prefix used for all resources in this environment"
  type        = string
  default     = "terraform"
}

variable "location" {
  description = "The Azure location where all resources in this deployment should be created"
  default     = "uksouth"
}

variable "flask_app" {
  description = "The FLASK_APP environment variable is used to specify how to load the application"
  type        = string
  default     = "app"
}

variable "flask_env" {
  description = "The FLASK_ENV environment variable is used to indicate to Flask what context Flask is running in"
  type        = string
  default     = "development"
}

variable "client_id" {
  description = "GitHub OAuth Client ID"
  type        = string
  sensitive   = true
}

variable "client_secret" {
  description = "GitHub OAuth Client Secret"
  type        = string
  sensitive   = true
}

variable "oathlib_insecure_transport" {
  description = "Use insecure transport for OAuth"
  type        = bool
  default     = true
}

variable "login_disabled" {
  description = "OAuth is used unless this is true"
  type        = bool
  default     = false
}

variable "loggly_token" {
  description = "Loggly Customer Access Token"
  type        = string
  sensitive   = true
}

variable "loggly_tag" {
  description = "Loggly tags to aid in segmentation and filtering"
  type        = string
  default     = "todo-app"
}