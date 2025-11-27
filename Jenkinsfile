pipeline {
    agent any
    
    environment {
        IMAGE_NAME = 'novamart-svc'
        IMAGE_TAG = '2'
        CONTAINER_NAME = 'novamart-container'
        HOST_PORT = '12072'
        CONTAINER_PORT = '5000'
    }
    
    stages {
        stage('Pre-check Docker') {
            steps {
                script {
                    echo '=== Checking Docker availability ==='
                    def dockerCheck = sh(script: 'docker --version', returnStatus: true)
                    if (dockerCheck != 0) {
                        error('Docker is not available! Please ensure Docker is installed and Jenkins has permission to access it.')
                    }
                    echo 'Docker is available'
                    
                    // Check Docker daemon connectivity
                    def dockerInfo = sh(script: 'docker info', returnStatus: true)
                    if (dockerInfo != 0) {
                        error('Cannot connect to Docker daemon! Check if Jenkins user is in docker group.')
                    }
                    echo 'Docker daemon is accessible'
                }
            }
        }
        
        stage('Checkout') {
            steps {
                echo '=== Checking out repository ==='
                checkout scm
                // Alternative: git branch: 'main', url: 'https://github.com/your-repo/novamart-app.git'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    echo '=== Building Docker image ==='
                    sh """
                        docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .
                    """
                    echo "Image ${IMAGE_NAME}:${IMAGE_TAG} built successfully"
                }
            }
        }
        
        stage('Stop Old Container') {
            steps {
                script {
                    echo '=== Stopping and removing old container if exists ==='
                    sh """
                        docker stop ${CONTAINER_NAME} 2>/dev/null || true
                        docker rm ${CONTAINER_NAME} 2>/dev/null || true
                    """
                }
            }
        }
        
        stage('Start Container') {
            steps {
                script {
                    echo '=== Starting new container ==='
                    sh """
                        docker run -d \
                            --name ${CONTAINER_NAME} \
                            -p ${HOST_PORT}:${CONTAINER_PORT} \
                            ${IMAGE_NAME}:${IMAGE_TAG}
                    """
                    echo "Container started on port ${HOST_PORT}"
                }
            }
        }
        
        stage('Verify Container') {
            steps {
                script {
                    echo '=== Verifying container is running ==='
                    sh """
                        docker ps | grep ${CONTAINER_NAME}
                    """
                    
                    echo '=== Checking port binding ==='
                    sh """
                        netstat -tuln | grep ${HOST_PORT} || ss -tuln | grep ${HOST_PORT}
                    """
                    
                    echo '=== Testing HTTP endpoint ==='
                    sleep 3  // Give the app a moment to start
                    sh """
                        curl -f http://localhost:${HOST_PORT}/ || echo "Warning: HTTP test failed"
                    """
                }
            }
        }
    }
    
    post {
        success {
            echo '=== Pipeline completed successfully ==='
            echo "NovaMart service is running at http://localhost:${HOST_PORT}"
        }
        failure {
            echo '=== Pipeline failed ==='
            script {
                sh """
                    docker logs ${CONTAINER_NAME} 2>/dev/null || echo "No container logs available"
                """
            }
        }
    }
}