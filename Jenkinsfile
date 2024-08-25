pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'us-east-1'
        ECR_REPO_NAME = 'hello-world'
        ECS_CLUSTER_NAME = 'hello-world-cluster'
        ECS_SERVICE_NAME = 'hello-world-service'
        IMAGE_TAG = "${env.BUILD_ID}"
        TF_WORKING_DIR = 'terraform/'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/your-github-username/autodeskproject.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${ECR_REPO_NAME}:${IMAGE_TAG}", "app/")
                }
            }
        }

        stage('Push Docker Image to ECR') {
            steps {
                script {
                    docker.withRegistry("https://${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com", 'ecr:us-east-1:aws-credentials') {
                        dockerImage.push("${IMAGE_TAG}")
                    }
                }
            }
        }

        stage('Terraform Init & Plan') {
            steps {
                dir("${TF_WORKING_DIR}") {
                    sh 'terraform init'
                    sh 'terraform plan -out=tfplan'
                }
            }
        }

        stage('Terraform Apply') {
            steps {
                dir("${TF_WORKING_DIR}") {
                    sh 'terraform apply tfplan'
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                script {
                    sh '''
                        aws ecs update-service \
                        --cluster ${ECS_CLUSTER_NAME} \
                        --service ${ECS_SERVICE_NAME} \
                        --force-new-deployment
                    '''
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
