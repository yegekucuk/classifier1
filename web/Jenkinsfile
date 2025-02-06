pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub')
        IMAGE_NAME = "yegekucuk2/classifier1-on-web"
    }

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }
        stage('Login to DockerHub') {
            steps {
                script {
                    sh "docker login -u ${DOCKERHUB_CREDENTIALS_USR} -p ${DOCKERHUB_CREDENTIALS_PSW}"
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    sh "docker push ${IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }
    }
}
