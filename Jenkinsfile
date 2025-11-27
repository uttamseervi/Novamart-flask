pipeline {
    agent any

    stages {

        stage('Pre-check Docker') {
            steps {
                sh '''
                if ! command -v docker &> /dev/null
                then
                    echo "❌ Docker not installed — FAILING PIPELINE"
                    exit 1
                else
                    echo "✔ Docker found:"
                    docker --version
                fi
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
                echo "🚀 Building Docker image novamart-svc:2"
                docker build -t novamart-svc:2 .
                '''
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                echo "🛑 Removing old container..."
                docker stop novamart-svc || true
                docker rm novamart-svc || true

                echo "🚀 Running new container on port 12072..."
                docker run -d -p 12072:5000 --name novamart-svc novamart-svc:2
                '''
            }
        }
    }

    post {
        success {
            echo "🎉 Pipeline SUCCESS!"
        }
        failure {
            echo "❌ Pipeline FAILED!"
        }
    }
}
