pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = 'hiuston007/flask-app'
    }

    stages {
        stage('Clone repo') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Login to DockerHub') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }

        stage('Push Docker image') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }
    }
}
