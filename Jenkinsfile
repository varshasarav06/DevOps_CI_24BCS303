pipeline {
agent any

stages {
    stage('Checkout') {
        steps {
            git branch: 'main', url: 'https://github.com/varshasarav06/DevOps_CI_24BCS303.git'
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
