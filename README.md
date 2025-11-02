# UOC LLM Security Framework

## Descripció

Aquest repositori proporciona un framework per avaluar i protegir models de text-a-imatge (LLMs) mitjançant guardrails i proves automatitzades. Inclou codi per a la selecció de models, configuració d’entorn, generació d’imatges i auditories de seguretat, tot integrat amb CI/CD via Jenkins.

## Característiques

- **Selecció de model:** Permet triar i descarregar models des de HuggingFace.
- **Configuració automatitzada:** Gestió d’entorn virtual Python i dependències.
- **Generació d’imatges:** Creació d’imatges a partir de prompts personalitzats.
- **Guardrails de seguretat:** Auditories de prompts i imatges generades amb scripts personalitzats.
- **Integració contínua:** Pipeline de Jenkins per a build, test i arxiu d’artefactes automàtic.

## Com començar

### Prerequisits

- Python 3.x
- [Compte HuggingFace](https://huggingface.co/) i token d’API
- Jenkins (per CI/CD)
- Git

### Instal·lació

1. **Clona el repositori:**
   ```bash
   git clone https://github.com/guillemhs/uoc-llm-security-framework.git
   cd uoc-llm-security-framework
   ```

2. **Configura l’entorn Python:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install --upgrade pip
   pip install -r requirements_images.txt
   pip install huggingface_hub[cli]
   ```

3. **Autenticació HuggingFace:**
   ```bash
   hf auth login --token <EL_TEUTOKEN>
   ```

### Ús

- **Descarregar un model:**
  ```bash
  python setup/download_model.py <NOM_DEL_MODEL>
  ```

- **Generar una imatge de mostra:**
  ```bash
  cd images
  python create_sample_image.py --prompt "El teu prompt aquí" --output "imatge_generada.png"
  cd ..
  ```

- **Executar guardrails:**
  ```bash
  python audit_images/prompt_guardrail.py "El teu prompt aquí"
  python audit_images/image_guardrail.py "images/imatge_generada.png"
  ```

### Pipeline Jenkins

El repositori inclou un Jenkinsfile per automatitzar els builds:

- **Etapes:**
  - Selecció de model
  - Checkout de codi
  - Configuració de l’entorn Python
  - Descarrega del model
  - Generació d’imatges
  - Auditories de guardrails
  - Arxiu d’imatges com a artefactes del build

Després de cada build, podràs descarregar les imatges generades des de Jenkins com a artefactes.

## Estructura del projecte

```
.
├── images/
│   ├── create_sample_image.py
│   └── generated_image_*.png
├── audit_images/
│   ├── prompt_guardrail.py
│   └── image_guardrail.py
├── setup/
│   └── download_model.py
├── requirements_images.txt
├── Jenkinsfile
└── README.md
```

## Contribució

Les pull requests són benvingudes. Si vols fer canvis importants, obre primer una issue per discutir-los.

## Llicència

Aquest codi ha estat alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota la llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional.

[![Llicència: CC BY-NC 4.0](https://img.shields.io/badge/License-CC_BY--NC_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/deed.ca)

Aquest fitxer README ha estat originalment redactat per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) i també està alliberat al domini públic.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).