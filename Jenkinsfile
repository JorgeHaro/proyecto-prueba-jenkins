pipeline {
    agent any

    stages {
        stage('Hola Mundo') {
            steps {
                echo "Hola Mundo desde la rama ${env.BRANCH_NAME}  y el commit ${env.GIT_COMMIT}"
            }
        }
    }
}
