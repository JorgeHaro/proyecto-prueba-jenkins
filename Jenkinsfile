pipeline {
    agent any

    stages {
        stage('Hola Dios') {
            steps {
                def branch = sh(script: "git rev-parse --abbrev-ref HEAD", returnStdout: true).trim()
                echo "Hola Dios, llamen a Dios, desde la rama ${branch}  y el commit ${env.GIT_COMMIT}"
            }
        }
    }
}
