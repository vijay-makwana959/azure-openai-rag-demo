pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t rag-app:${BRANCH_NAME} .'
      }
    }

    stage('Push Image') {
      when {
        branch 'main'
      }
      steps {
        sh '''
        docker tag rag-app:main myacr.azurecr.io/rag-app:latest
        docker push myacr.azurecr.io/rag-app:latest
        '''
      }
    }

    stage('Deploy') {
      when {
        branch 'main'
      }
      steps {
        echo "Deploying to Azure App Service / AKS"
      }
    }
  }
}
