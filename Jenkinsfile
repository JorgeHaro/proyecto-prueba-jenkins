pipeline {
    agent any

    stages {
        stage('Hola Dios') {
            steps {
                script {
                    def branch = env.GIT_BRANCH ?: 'desconocida'
                    echo "Hola Dios, llamen a Dios, desde la rama ${branch} y el commit ${env.GIT_COMMIT}"
                }
            }
        }
    }
}
