pipeline {
    agent any

    environment {
        IMAGE_NAME = 'novamart-svc:2'
        CONTAINER_NAME = 'novamart-svc-container'
        PORT = '12072'
    }

    stages {
        stage('Pre-check Docker') {
            steps {
                script {
                    def dockerCheck = sh(script: 'docker --version', returnStatus: true)
                    if (dockerCheck != 0) {
                        error "Docker is not available. Please install/start Docker."
                    }
                }
            }
        }

      stage('Checkout') {
    steps {
        git branch: 'main',
            url: 'https://github.com/uttamseervi/Novamart-flask.git',
            credentialsId: 'e4974bdd-8b4a-47fa-aa47-157c58c31966'
    }
}


        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${IMAGE_NAME} ."
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Stop and remove any existing container with same name
                    sh "docker rm -f ${CONTAINER_NAME} || true"
                    sh "docker run -d -p ${PORT}:${PORT} --name ${CONTAINER_NAME} ${IMAGE_NAME}"
                }
            }
        }

        stage('Verify Container') {
            steps {
                sh "docker ps | grep ${CONTAINER_NAME}"
                sh "curl -s http://localhost:${PORT} || echo 'Flask service not responding'"
            }
        }
    }

    post {
        failure {
            echo "Pipeline failed."
        }
    }
}
