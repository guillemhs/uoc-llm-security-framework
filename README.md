# UOC LLM Security Framework

Framework lleuger per avaluar i protegir workflows de models de text-a-imatge mitjançant guardrails i proves automatitzades. Inclou scripts per seleccionar i descarregar models (Hugging Face), generar imatges a partir de prompts i auditar tant els prompts com les imatges generades. Disposa de pipelines de Jenkins per a integració contínua amb artefactes versionats.

---

## ✨ Característiques clau
- Selecció i descarrega de models des de Hugging Face.
- Generació d’imatges a partir de prompts personalitzats.
- Guardrails de seguretat sobre prompts i imatges.
- Integració amb Jenkins per a CI/CD (build, test, artefactes).
- Estructura modular i scripts simples d’utilitzar.

---

## 🧩 Estructura del repositori
- setup/
  - download_model.py — Descarrega un model de Hugging Face.
- images/
  - create_sample_image.py — Genera imatges a partir d’un prompt.
  - generated_image_*.png — Sortides generades (artefactes).
- audit_images/
  - prompt_guardrail.py — Audita el prompt (seguretat i conformitat).
  - image_guardrail.py — Audita la imatge generada.
- utils/ — Utilitats comunes (si escau).
- audit_text/ — Auditories per a text (si escau).
- requirements_images.txt — Dependències per al flux d’imatges.
- requirements_text.txt — Dependències per al flux de text.
- JenkinsfileImages, JenkinsfileText — Pipelines de Jenkins (variants).
- README.md — Aquest document.

---

## 📋 Prerequisits
- Python 3.x
- Git
- Compte de Hugging Face i token d’API
- Jenkins (opcional, per a CI/CD)

---

## 🚀 Instal·lació i posada en marxa

1) Clona el repositori
- git clone https://github.com/guillemhs/uoc-llm-security-framework.git
- cd uoc-llm-security-framework

2) Crea l’entorn Python
- python3 -m venv venv
- source venv/bin/activate
- pip install --upgrade pip
- pip install -r requirements_images.txt
- pip install "huggingface_hub[cli]"

3) Autentica’t a Hugging Face
- hf auth login --token <EL_TEUTOKEN>

---

## 🛠️ Ús bàsic

1) Descarregar un model
- python setup/download_model.py <NOM_DEL_MODEL>
Exemple: python setup/download_model.py runwayml/stable-diffusion-v1-5

2) Generar una imatge
- cd images
- python create_sample_image.py --prompt "Un robot llegint un llibre en una biblioteca futurista" --output "imatge_generada.png"
- cd ..

3) Executar guardrails
- Prompt: python audit_images/prompt_guardrail.py "Un robot llegint un llibre en una biblioteca futurista"
- Imatge: python audit_images/image_guardrail.py "images/imatge_generada.png"

Els scripts retornen informació de validació o alertes. Integra aquesta sortida als teus informes o al pipeline de CI.

---

## 🔐 Guardrails i criteris de seguretat
Aquest framework aplica controls en dos punts:
- Abans de generar: avaluació del prompt per detectar continguts no permesos (p. ex., violència extrema, contingut sexual explícit, incitació a l’odi, etc.).
- Després de generar: avaluació de la imatge per detectar continguts problemàtics (p. ex., NSFW, violència, marques registrades, privacitat).

Notes:
- Els criteris exactes depenen de la implementació dels scripts d’auditoria i, si s’han configurat, de models/clasificadors auxiliars.
- Ajusta llindars i categories segons les teves necessitats de compliment (p. ex., polítiques internes, legals o de plataforma).

---

## 🔄 Integració amb Jenkins (CI/CD)

Aquest repositori inclou Jenkinsfiles per automatitzar:
1) Checkout i configuració d’entorn Python net.
2) Selecció i descarrega del model de Hugging Face.
3) Generació d’imatges amb prompts definits (paràmetres del job).
4) Execució dels guardrails de prompt i d’imatge.
5) Publicació de les imatges i dels logs de validació com a artefactes.

Bones pràctiques:
- Parametritza el nom del model i el prompt al job.
- Desa els artefactes (imatges, informes JSON/HTML) per a traçabilitat.
- Fixa versions de models (revision/commit de Hugging Face) per reproductibilitat.

---

## 🧪 Exemples de comandes

- Descarregar model:
  - python setup/download_model.py runwayml/stable-diffusion-v1-5

- Generar imatge:
  - python images/create_sample_image.py --prompt "Un paisatge al capvespre amb drons" --output "sunset_drones.png"

- Auditar prompt:
  - python audit_images/prompt_guardrail.py "Un paisatge al capvespre amb drons"

- Auditar imatge:
  - python audit_images/image_guardrail.py "images/sunset_drones.png"

---

## 🔧 Configuració i variables d’entorn
- HF_TOKEN — Token de Hugging Face (si no uses `hf auth login`).
- MODEL_ID — Identificador del model (per a pipelines).
- PROMPT — Prompt d’entrada (per a pipelines).
- OUTPUT_PATH — Ruta per desar la imatge generada.

Pots definir-les a Jenkins com a paràmetres o credencials segures.

---

## Probes per al Smoke Test

Les probes utilitzades pel smoke test són les següents:

- `dan.DAN_Jailbreak`
- `dan.ChatGPT_Developer_Mode_v2`
- `encoding.InjectBase64`
- `promptinject.HijackHateHumansMini`
- `realtoxicityprompts.RTPInsult`
- `knownbadsignatures.EICAR`
- `malwaregen.TopLevel`
- `packagehallucination.Python`
- `xss.MarkdownImageExfil`

Comanda per executar el smoke test amb aquestes probes:

```bash
python3 -m garak --model_type huggingface --model_name openai-community/gpt2 --probes dan.DAN_Jailbreak,dan.ChatGPT_Developer_Mode_v2,encoding.InjectBase64,promptinject.HijackHateHumansMini,realtoxicityprompts.RTPInsult,knownbadsignatures.EICAR,malwaregen.TopLevel,packagehallucination.Python,xss.MarkdownImageExfil
```
 
## Models sota anàlisi

Models proposats per a l’anàlisi i proves:

- `openai-community/gpt2`
- `Qwen/Qwen3-0.6B`
- `Gensyn/Qwen2.5-0.5B-Instruct`
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- `meta-llama/Llama-3.2-1B-Instruct`
- `distilbert/distilgpt2`
- `google/gemma-3-1b-it`

---

## 📐 Bones pràctiques i consells
- Mantén una suite de prompts de prova: segurs, borderline i prohibits, per validar els guardrails.
- Registra logs i decisions dels guardrails; genera informes en JSON/HTML per als artefactes.
- Estableix llindars clars i documenta’ls (què es marca, què es bloqueja).
- Controla versions de models i dependències per assegurar consistència.

---

## ❓ Preguntes freqüents (FAQ)
- El framework només és per a imatges?
  - L’enfoc principal és text-a-imatge. Hi ha fitxers de requirements i carpetes per a text si vols ampliar-ho.

- Necessito GPU?
  - Depèn del model i del volum. Molts models de text-a-imatge es beneficien d’una GPU, però també pots provar amb CPU (més lent).

- Puc canviar el model fàcilment?
  - Sí, el script de descarrega accepta qualsevol MODEL_ID de Hugging Face.

---

## 🤝 Contribució
Les pull requests són benvingudes. Per canvis majors, obre primer una issue per discutir-los. Si afegeixes nous guardrails, adjunta exemples i tests mínims.

Passos recomanats:
- Fes un fork i crea una branca feature/… o fix/…
- Assegura’t que els scripts s’executen sense errors
- Afegeix o actualitza documentació i exemples

---

## 📄 Llicència i autoria
Aquest codi és alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional (CC BY-NC 4.0).  

El README ha estat redactat per a aquest repositori i segueix la mateixa llicència.

Per a més informació o contacte, consulta el perfil de l’autor al repositori.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).