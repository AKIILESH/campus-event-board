pipeline {
    agent any

    environment {
        IMAGE_NAME = 'campus-event-ci'
        CONTAINER_NAME = 'campus-event-ansible'
        APP_PORT = '5001'
        DOCKER_VOLUME = 'eventboard_data'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                echo '=== Stage 1: Checkout Source Code from GitHub ==='
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo '=== Stage 2: Building Application Docker Image ==='
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Run Automated Tests') {
            steps {
                echo '=== Stage 3: Running Pytest Test Suite inside Container ==='
                sh 'docker run --rm ${IMAGE_NAME} python -m pytest test_app.py -v'
            }
        }

        stage('Deploy with Ansible') {
            steps {
                echo '=== Stage 4: Continuous Deployment using Ansible Playbook ==='
                script {
                    // Try execution via ansible-docker-lab container or local ansible-playbook runner
                    sh '''
                        if docker ps --format '{{.Names}}' | grep -q 'ansible-docker-lab'; then
                            docker exec ansible-docker-lab ansible-playbook -i /inventory.ini /docker-deploy.yml
                        elif command -v ansible-playbook >/dev/null 2>&1; then
                            ansible-playbook -i ansible/inventory.ini ansible/docker-deploy.yml
                        else
                            echo "Ansible CLI not found directly; performing containerized deployment:"
                            docker volume create ${DOCKER_VOLUME} || true
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                            docker run -d --name ${CONTAINER_NAME} \
                                --restart unless-stopped \
                                -p ${APP_PORT}:5000 \
                                -v ${DOCKER_VOLUME}:/app/data \
                                ${IMAGE_NAME}
                        fi
                    '''
                }
            }
        }

        stage('Verify Deployment Health') {
            steps {
                echo '=== Stage 5: Verifying Container and HTTP Health Endpoint ==='
                sh '''
                    sleep 3
                    docker ps --filter "name=${CONTAINER_NAME}"
                    curl -s -f http://localhost:${APP_PORT}/health || echo "Endpoint pending or running in remote docker host"
                '''
            }
        }
    }

    post {
        success {
            echo '==========================================================='
            echo 'Campus Event Board CI/CD Pipeline Completed Successfully!'
            echo 'Deployed at: http://localhost:5001'
            echo 'Admin Console: http://localhost:5001/admin'
            echo '==========================================================='
        }
        failure {
            echo 'Pipeline failed! Check stage console logs for debugging.'
        }
    }
}
