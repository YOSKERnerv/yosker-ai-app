pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/YOSKERnerv/yosker-ai-app.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${env.GIT_REPO}"
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t yosker-ai-app .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up -d --build'
            }
        }
    }

    post {
        failure {
            echo 'Build failed!'
        }
        success {
            echo 'Deployment successful!'
        }
    }
}
