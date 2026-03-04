pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

    }

    post {

        always {
            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Automation Test Report'
            ])
        }

        failure {
            echo 'Build Failed'
        }

        success {
            echo 'Build Successful'
        }
    }
}