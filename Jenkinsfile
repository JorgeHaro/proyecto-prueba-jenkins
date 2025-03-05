pipeline {
    agent any

    stages {
        stage('Hola Mondo') {
            steps {
                script {
                    def commitMessage = sh(script: "git log -1 --pretty=%B", returnStdout: true).trim()

                    echo "Este es el mensaje => ${commitMessage}"

                    if (commitMessage.contains("Merge")) {
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
