pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            checkout scm
        }
    }

    stage('Build') {
        steps {
            echo 'Build successful'
        }
    }

    stage('Test') {
        steps {
            sh 'python3 -m unittest discover -s tests'
        }
    }

    stage('Result') {
        steps {
            echo 'Pipeline completed successfully'
        }
    }
}

}
