pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git 'https://github.com/Surya-Sastry/JenkinsDemo.git'
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x Demo.py"
                sh "python3 Demo.py"
            }
        }
        stage('Test Code 1') {
            steps {
                sh "chmod u+x PassTest.py"
                sh "python3 PassTest.py"
            }
        }
        stage('Test Code 2') {
            steps {
                sh "chmod u+x FailTest.py"
                sh "python3 FailTest.py"
            }
        }
    } 
}
