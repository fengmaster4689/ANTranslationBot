provider "aws" {
  region = "us-east-1"
}

resource "aws_lightsail_instance" "AWS-ANTrans" {
  name              = "AWS-ANTrans-instance"
  availability_zone = "us-east-1a"
  blueprint_id      = "amazon_linux_2023"
  bundle_id         = "micro_3_0"
  tags = {
    name = "Discord"
  }
}