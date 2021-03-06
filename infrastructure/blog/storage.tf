resource "azurerm_storage_account" "blog" {
  name                     = "an0rakblog"
  resource_group_name      = var.az_resource_group
  location                 = var.az_location
  account_tier             = "Standard"
  account_kind             = "StorageV2"
  account_replication_type = "LRS"

  static_website {
    index_document     = "index.html"
    error_404_document = "404.html"
  }

  tags = {
    creator = "terraform"
    purpose = "blog"
  }
}

resource "azurerm_cdn_profile" "blog_cdn" {
  name                = "blogCdn"
  location            = var.az_location
  resource_group_name = var.az_resource_group
  sku                 = "Standard_Microsoft"
}

resource "azurerm_cdn_endpoint" "blog_endpoint" {
  name                = "an0rak-cdn-endpoint"
  profile_name        = azurerm_cdn_profile.blog_cdn.name
  location            = var.az_location
  resource_group_name = var.az_resource_group
  origin {
    name      = "blog"
    host_name = azurerm_storage_account.blog.primary_web_host
  }
}

output "CDN_Endpoint" {
  value = azurerm_cdn_endpoint.blog_endpoint.fqdn
}