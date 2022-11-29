terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "2.23.1"
    }
  }
}

#self-signed, key ID BD080C4571C6104C
provider "docker" {
  host    = "npipe:////.//pipe//docker_engine"
}

# Pulls the image
resource "docker_image" "ubuntu" {
  name = "ubuntu:latest"
}

# Create a container
resource "docker_container" "server-container" {
  image             = docker_image.ubuntu.image_id
  name              = "terraform-docker-test"
  must_run          = true
  publish_all_ports = true
  command = [
    "sleep",
    "30"
  ]
}