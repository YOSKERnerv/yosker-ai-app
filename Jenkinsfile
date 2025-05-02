pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/YOSKERnerv/yosker-ai-app.git'
        DOCKERHUB_USER = 'yoskernervo'
        IMAGE_NAME = 'yosker_ai_app'
        TAG = "${BUILD_NUMBER}"  // tag with Jenkins build number
    }

    stages {
        stage('Clone Repository') {
            steps {
                git url: "${env.GIT_REPO}", branch: 'main'
            }
        }

        stage('Verify Docker Installation') {
            steps {
                bat 'docker --version'
                bat 'docker-compose --version'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %DOCKERHUB_USER%/%IMAGE_NAME%:%TAG% ."
            }
        }

        stage('Run Tests') {
            steps {
                echo '🔍 Running containerized tests...'
                bat "docker run --rm %DOCKERHUB_USER%/%IMAGE_NAME%:%TAG% python -m unittest discover tests"
            }
        }

        stage('Run Docker Compose') {
            steps {
                bat 'docker-compose down'
                bat 'docker-compose up -d --build'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    bat 'echo %PASSWORD% | docker login -u %USERNAME% --password-stdin'
                    bat "docker tag %DOCKERHUB_USER%/%IMAGE_NAME%:%TAG% %USERNAME%/%IMAGE_NAME%:%TAG%"
                    bat "docker push %USERNAME%/%IMAGE_NAME%:%TAG%"
                    bat 'docker logout'
                }
            }
        }
    }

    post {
        failure {
            echo '❌ Build failed!'
        }
        success {
            echo "✅ Deployment successful and Docker image pushed to Docker Hub with tag: ${env.TAG}"
        }
    }
}
