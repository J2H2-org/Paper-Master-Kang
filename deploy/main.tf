locals {
    vpc_id              = "vpc-04092f12e5e3c0e10"
    subnet_id           = "subnet-09a7cc707ae950334"
    ssh_user            = "root"
    key_name            = "deploy_1"
    private_key_path    = "./keys/deploy_1.pem"
}

provider "aws" {
    region = "ap-northeast-2"
}

resource "aws_security_group" "nginx" {
    name    = "nginx_access"
    vpc_id  = local.vpc_id

    ingress {
        from_port   = 22
        to_port     = 22
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    ingress {
        from_port   = 80
        to_port     = 80
        protocol    = "tcp"
        cidr_blocks = ["0.0.0.0/0"]
    }

    egress {
        from_port   = 0
        to_port     = 0
        protocol    = "-1"
        cidr_blocks = ["0.0.0.0/0"]
    }
}

resource "aws_instance" "nginx" {
    ami                           = "ami-0454bb2fefc7de534"
    subnet_id                     = local.subnet_id
    instance_type                 = "t2.micro"
    associate_public_ip_address   = true

    provisioner "remote-exec" {
        inline = ["echo 'Wait until SSH is ready'"]

        connection {
            type        = "ssh"
            user        = local.ssh_user
            private_key = file(local.private_key_path)
            host        = aws_instance.nginx.public_ip
        }
    }

    provisioner "local-exec" {
        command = "ansible-playbook  -i ${aws_instance.nginx.public_ip}, --private-key ${local.private_key_path} nginx.yaml"
    }
}

output "nginx_ip" {
    value = aws_instance.nginx.public_ip
}