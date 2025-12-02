# UOC LLM Security Framework

![Python Version](https://img.shields.io/badge/python-3.12%2B-blue)
![License](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)
![Institution](https://img.shields.io/badge/UOC-Màster_Ciberseguretat-red)
![Status](https://img.shields.io/badge/Status-Completed-success)

Aquest repositori conté el codi font, els scripts d'auditoria i els resultats experimentals desenvolupats com a part del **Treball Final de Màster (TFM)** del Màster Universitari en Ciberseguretat i Privadesa de la **Universitat Oberta de Catalunya (UOC)**.

**Títol del Projecte:** Anàlisi de riscos i disseny d'un framework de seguretat per a la implementació de GenAI en entorns empresarials.

## 📋 Descripció del Projecte

L'objectiu d'aquest projecte és auditar la seguretat dels models d'Intel·ligència Artificial Generativa (GenAI) de codi obert (*Open Source*) i demostrar la necessitat d'implementar controls externs (*Guardrails*) abans del seu desplegament en producció.

El treball s'ha centrat en dues verticals:
1.  **Models de Text (LLM):** Avaluació de vulnerabilitats com *Prompt Injection*, *Jailbreaking* i *Package Hallucination* en models com **Qwen 2.5**, **Llama 3.2** i **TinyLlama**.
2.  **Models d'Imatge (Diffusion):** Anàlisi de la generació de contingut nociu (NSFW) i riscos de seguretat en models com **Stable Diffusion XL (SDXL)** i **Animagine XL**.

## 📂 Estructura del Repositori

```bash
.
├── audit_images/                 
├── deprecated/                   
├── setup/                   
├── utils/      
├── requirements.txt        
├── ttimages_batch_smokes_scan.sh        
├── ttt_batch_smokes_scan.sh        
├── ttt_batch_test_scan.sh        
└── README.md               
```

# 🚀 Instal·lació i Requisits
El projecte s'ha desenvolupat i testejat en un entorn local Apple tant per  Apple Silicon M1/M2/M3 com per Apple Intel utilitzant Python 3.12.

# Prerequisits
```
Python 3.12+
venv
(Opcional) Accés a GPU per a una inferència més ràpida.
```

## Configuració de l'entorn
# Clonar el repositori
```
git clone https://github.com/guillemhs/uoc-llm-security-framework.git
cd uoc-llm-security-framework
```

# Crear un entorn virtual
```
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

# Instal·lar dependències
```
pip install -r requirements.txt
```

*NOTA*: Més informació en el fitxer ```install_venv.sh```

*NOTA 2*: Es necessita un *HUGGINGFACE_HUB_TOKEN* perquè descarregar automàticament els models.

# 🛠️ Ús i Execució
1. En l'arxiu ```JenkinsfileText``` hi ha l'auditoria de Models de Text-to-Text fent servir [Garak](https://github.com/NVIDIA/garak)  

```
        // Etapa 3: Descarregar el model de HuggingFace
        stage('Download HuggingFace Model') {
            steps {
                sh """ source ./venv/bin/activate && hf auth login --token $HUGGINGFACE_HUB_TOKEN """ 
                sh """ export HUGGINGFACE_HUB_TOKEN=$HUGGINGFACE_HUB_TOKEN """
                sh """ echo 'Descarregar el model de HuggingFace ${env.MODELS}' """
                sh """ . venv/bin/activate && ${PYTHON} setup/download_model.py ${env.MODELS} """
            } 
        }

        // Etapa 4: Execució de Garak
        stage('Garak Check') {
            steps {
                sh """ echo 'Execució de la prova de Garak a ${env.MODELS}' """
                sh """. venv/bin/activate && ./run_garak.sh ${env.MODELS} $PROBES | tee logs_${env.MODELS}.txt """
            }
        }
```

2. Auditoria de Models d'Imatge
En l'arxiu ```JenkinsfileImage``` hi ha l'auditoria de Models de Text-to-Image fent servir una solució pròpia basada en [Garak](https://github.com/NVIDIA/garak) 

```
        // Etapa 3: Descarregar el model de HuggingFace
        stage('Download HuggingFace Model') {
            steps {
                sh """ source ./venv/bin/activate && hf auth login --token $HUGGINGFACE_HUB_TOKEN """ 
                sh """ export HUGGINGFACE_HUB_TOKEN=$HUGGINGFACE_HUB_TOKEN """
                sh """ echo 'Descarregar el model de HuggingFace ${env.MODELS}' """
                sh """ . venv/bin/activate && ${PYTHON} setup/download_text_to_image_model.py ${env.MODELS} """
            } 
        }

        // Etapa 4: Execució de les proves de scripts
        stage('Script Check') {
            steps {
                sh """ echo 'Execució de la prova de Garak a ${env.MODELS}' """
                sh """. venv/bin/activate && ${PYTHON} audit_images/probes.py ${env.MODELS} >> logs_${env.MODELS}.txt """
            }
        }
```

## 👤 Autor
[Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/)

[Màster en Ciberseguretat i Privadesa (UOC)](https://www.uoc.edu/ca/estudis/masters/master-universitari-ciberseguretat-privadesa-landmkt?esl-k=google-ads%7Cng%7Cc570858264445%7Cmp%7Ckmaster%20uoc%20ciberseguretat%7Cp%7Ct%7Cdc%7Ca133062043564%7Cg15285581959&utm_medium=cpc&utm_source=googlebrand&utm_campaign=cap_mu_ca&utm_term=master%20uoc%20ciberseguretat&gad_source=1&gad_campaignid=15285581959&gbraid=0AAAAAD_RHGJbHzGmeCevXcHUrxTK9xoeb&gclid=Cj0KCQiAubrJBhCbARIsAHIdxD8aL4fFCIP_pQ7_jvgkuWAB4XQah0Isn8MqZnRzV4vDBwUNhYivFeMaAl_yEALw_wcB)

[GitHub: @guillemhs](https://github.com/guillemhs)

## 📄 Llicència i autoria

Aquest repositori forma part de l'avaluació acadèmica de la Universitat Oberta de Catalunya. Els models i scripts s'han d'utilitzar únicament amb finalitats de recerca i auditoria ètica.

Aquest codi és alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional (CC BY-NC 4.0).  

El README ha estat redactat per a aquest repositori i segueix la mateixa llicència.

Per a més informació o contacte, consulta el perfil de l’autor al repositori.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).

## Contacte
Per dubtes o col·laboració: obre una issue al repositori o contacta amb els mantenidors indicats a la documentació.