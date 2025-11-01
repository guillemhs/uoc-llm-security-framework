pipeline {
    agent any

    environment {
        PYTHON = 'python3' // Defineix la versió de Python a utilitzar
    }

    stages {
        // Etapa 0: Selecció del model
        stage('Model Selection') {
            steps {
                sh "echo 'Model: ${env.MODELS}'"
            }
        } 

        // Etapa 1: Clonar el codi del repositori
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/guillemhs/uoc-llm-security-framework.git', branch: 'main'
            }
        } 

        // Etapa 2: Configurar l'entorn virtual Python
        stage('Setup Python Environment') {
            steps {
                sh '${PYTHON} -m venv venv' // Crear l'entorn virtual
                sh '. venv/bin/activate && pip install --upgrade pip' // Actualitzar pip
                sh '. venv/bin/activate && pip install -r requirements.txt' // Instal·lar dependències
            }
        }

        // Etapa 3: Descarregar el model de HuggingFace
        stage('Download HuggingFace Model') {
            steps {
                sh """ . venv/bin/activate && ${PYTHON} setup/download_model.py ${env.MODELS} """
            } 
        }

        // Etapa 4: Execució de la prova de prompt injection
        stage('Prompt Injection Check') {
            steps {
                sh """. venv/bin/activate && ${PYTHON} audit/prompt_injection.py ${env.MODELS} """
            }
        }

        // Etapa 5: Execució de la prova de toxicitat
        stage('Toxicity Check') {
            steps {
                sh """. venv/bin/activate && ${PYTHON} audit/toxicity.py ${env.MODELS} """
            }
        }

        // Etapa 6: Execució de la prova de biaixos
        stage('Bias Check') {
            steps {
                sh """. venv/bin/activate && ${PYTHON} audit/bias.py ${env.MODELS} """
            }
        }

        // Etapa 7: Execució de la prova de fugues de dades
        stage('Data Leakage Check') {
            steps {
                sh """. venv/bin/activate && ${PYTHON} audit/data_leakage.py ${env.MODELS} """
            }
        }

        // Etapa 8: Agregar resultats
        stage('Aggregate Results') {
            steps {
                sh '. venv/bin/activate && ${PYTHON} utils/aggregate_results.py'
            }
        }

        // Etapa 9: Arxivar resultats
        stage('Archive Results') {
            steps {
                archiveArtifacts artifacts: 'results/*.json', allowEmptyArchive: true
            }
        }
    }

    // Post-execució: enviar notificacions o netejar recursos
    post {
        success {
            echo 'Pipeline completat amb èxit!'
        }
        failure {
            echo 'El pipeline ha fallat. Revisa els logs per trobar el problema.'
        }
    }
}