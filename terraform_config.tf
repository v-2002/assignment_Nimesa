provider "aws" {
  region = "ap-south-1"  
}

resource "aws_vpc" "example_vpc" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.example_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "ap-south-1"  
}

resource "aws_subnet" "private_subnet" {
  vpc_id                  = aws_vpc.example_vpc.id
  cidr_block              = "10.0.2.0/24"
  availability_zone       = "ap-south-1"  
}

resource "aws_security_group" "example_sg" {
  vpc_id = aws_vpc.example_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
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

resource "aws_instance" "example_instance" {
  ami           = "ami-0323c3dd2da7fb37d"  
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id
  vpc_security_group_ids = [aws_security_group.example_sg.id]

  root_block_device {
    volume_size = 8
    volume_type = "gp2"
    delete_on_termination = true
  }

  tags = {
    Name    = "ExampleInstance"
    purpose = "Assignment"
  }
}
