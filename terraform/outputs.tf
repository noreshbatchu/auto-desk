# terraform/outputs.tf

output "vpc_id" {
  value = aws_vpc.main.id
}

output "jenkins_public_ip" {
  value = aws_instance.jenkins.public_ip
}
