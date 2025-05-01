pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/YOSKERnerv/yosker-ai-app.git'
        POWERSHELL_PATH = 'C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe'
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${env.GIT_REPO}", branch: 'main'
            }
        }

        stage('Verify Docker Installation') {
            steps {
                bat "${env.POWERSHELL_PATH} -Command \"docker --version\""
                bat "${env.POWERSHELL_PATH} -Command \"docker-compose --version\""
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "${env.POWERSHELL_PATH} -Command \"docker build -t yosker-ai-app .\""
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat "${env.POWERSHELL_PATH} -Command \"docker-compose down || exit 0\""
                bat "${env.POWERSHELL_PATH} -Command \"docker-compose up -d --build\""
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
