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

2. Auditoria de Models d'Imatge
En l'arxiu ```JenkinsfileImage``` hi ha l'auditoria de Models de Text-to-Image fent servir una solució pròpia basada en [Garak](https://github.com/NVIDIA/garak) 

## 👤 Autor
Guillem Hernández Sola
Màster en Ciberseguretat i Privadesa (UOC)
GitHub: @guillemhs

## 📄 Llicència i autoria

Aquest repositori forma part de l'avaluació acadèmica de la Universitat Oberta de Catalunya. Els models i scripts s'han d'utilitzar únicament amb finalitats de recerca i auditoria ètica.

Aquest codi és alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional (CC BY-NC 4.0).  

El README ha estat redactat per a aquest repositori i segueix la mateixa llicència.

Per a més informació o contacte, consulta el perfil de l’autor al repositori.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).

## Contacte
Per dubtes o col·laboració: obre una issue al repositori o contacta amb els mantenidors indicats a la documentació.