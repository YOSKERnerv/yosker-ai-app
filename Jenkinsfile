pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/YOSKERnerv/yosker-ai-app.git'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${env.GIT_REPO}", branch: 'main'
            }
        }

        stage('Verify Docker Installation') {
            steps {
                powershell 'docker --version'
                powershell 'docker-compose --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                powershell 'docker build -t yosker-ai-app .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                powershell 'docker-compose down || exit 0'
                powershell 'docker-compose up -d --build'
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed!'
        }
        success {
            echo '✅ Deployment successful!'
        }
    }
}
