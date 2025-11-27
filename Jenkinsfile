pipeline {
    agent any

    stages {

        stage('Pre-check Docker') {
            steps {
                sh '''
                if ! command -v docker &> /dev/null
                then
                    echo "Docker not installed — FAILING PIPELINE"
                    exit 1
                fi
                docker --version
                '''
            }
        }

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                echo "Building image novamart-svc:2"
                docker build -t novamart-svc:2 .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                echo "Stopping old container (if exists)..."
                docker stop novamart-svc || true
                docker rm novamart-svc || true

                echo "Starting new container..."
                docker run -d -p 12072:5000 --name novamart-svc novamart-svc:2
                '''
            }
        }
    }

    post {
        success {
            echo "NovaMart CI Pipeline completed successfully."
        }
    }
}
