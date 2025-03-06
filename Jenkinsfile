pipeline {
    agent any

    stages {
        stage('Verificar Merge') {
            steps {
                script {

                    sh 'git fetch --unshallow || true'

                    def parentCount = sh(script: "git rev-list --parents -n 1 HEAD | awk '{print NF-1}'", returnStdout: true).trim()

                    echo "Numero de padres: ${parentCount}"

                    if (parentCount.toInteger() > 1) {
                        echo "Hola Mundo, ¡Se ha hecho un MERGE en la rama deploy!"
                    } else {
                        echo "No es un merge, el pipeline no se ejecutará."
                        currentBuild.result = 'ABORTED'
                    }
                }
            }
        }
    }
}
