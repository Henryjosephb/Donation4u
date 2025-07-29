pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/yourusername/yourrepo.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build('donation4u-web:latest')
                }
            }
        }

        stage('Run Tests') {
            steps {
                // If you have tests, run them here
                echo 'No tests configured yet'
            }
        }

        stage('Push Docker Image') {
            steps {
                // If you use DockerHub or any registry, add push steps here
                echo 'Add Docker push steps here if needed'
            }
        }

        stage('Deploy') {
            steps {
                // Deployment steps (e.g., ssh to server and docker-compose up)
                echo 'Deploy steps go here'
            }
        }
    }
}
