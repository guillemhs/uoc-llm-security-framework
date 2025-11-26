# UOC LLM Security Framework

Framework lleuger per avaluar i protegir workflows de models de text-a-imatge mitjançant guardrails i proves automatitzades. Inclou scripts per seleccionar i descarregar models (Hugging Face), generar imatges a partir de prompts i auditar tant els prompts com les imatges generades. Disposa de pipelines de Jenkins per a integració contínua amb artefactes versionats.

---

## ✨ Característiques clau
- Selecció i descarrega de models des de Hugging Face.
- Generació d’imatges a partir de prompts simples.
- Guardrails de seguretat sobre prompts i imatges.
- Integració amb Jenkins per a CI/CD (build, test, artefactes).
- Estructura modular i scripts simples d’utilitzar.

---

## 🧩 Estructura del repositori (fitxers rellevants)
- setup/
  - [`download_model`](setup/download_model.py) — [setup/download_model.py](setup/download_model.py) (descarrega models LLM)
  - [`download_image_model`](setup/download_text_to_image_model.py) — [setup/download_text_to_image_model.py](setup/download_text_to_image_model.py) (descarrega models de diffusers)
- images/
  - [create_sample_image.py](images/create_sample_image.py) — genera una imatge de mostra (actualment crea `sample.png`)
- audit_images/
  - [probes.py](audit_images/probes.py) — suite de proves per a models d'imatge
  - versions de guardrails en [audit_images/deprecated/](audit_images/deprecated/)
- audit_text/
  - [bias.py](audit_text/bias.py), [data_leakage.py](audit_text/data_leakage.py), [prompt_injection.py](audit_text/prompt_injection.py), [toxicity.py](audit_text/toxicity.py), [run_garak.py](audit_text/run_garak.py)
- utils/
  - [aggregate_results.py](utils/aggregate_results.py)
  - [test_client.py](utils/test_client.py)
- scripts de control i batches:
  - [run_garak.sh](run_garak.sh)
  - [ttt_batch_smokes_scan.sh](ttt_batch_smokes_scan.sh)
  - [ttimages_batch_smokes_scan.sh](ttimages_batch_smokes_scan.sh)
  - [ttt_batch_test_scan.sh](ttt_batch_test_scan.sh)
- Jenkinsfiles:
  - [JenkinsfileText](JenkinsfileText)
  - [JenkinsfileImages](JenkinsfileImages)
  - [JenkinsGarakSmoke](JenkinsGarakSmoke)
  - [JenkinsGarakTest](JenkinsGarakTest)
- configuració / llistes:
  - [models.txt](models.txt)
  - [smoke_list_probes.txt](smoke_list_probes.txt)
  - [requirements_images.txt](requirements_images.txt), [requirements_text.txt](requirements_text.txt), [requirements.txt](requirements.txt)

---

## 📋 Prerequisits
- Python 3.12+ recomanat (els scripts d'exemple i `install_venv.sh` apunten a 3.12)
- Git
- Compte de Hugging Face i token d’API
- Opcional: GPU per a models grans (CUDA/MPS)

---

## 🚀 Instal·lació ràpida

1) Clona el repositori
- git clone https://github.com/guillemhs/uoc-llm-security-framework.git
- cd uoc-llm-security-framework

2) Crea i activa l'entorn Python
- python3.12 -m venv venv
- source venv/bin/activate
- pip install --upgrade pip

3) Instal·la dependències segons el flux:
- Per imatges: pip install -r requirements_images.txt
- Per text: pip install -r requirements_text.txt
- Si vols tot: pip install -r requirements.txt

4) Autentica’t a Hugging Face (opcional si ja fas `hf auth login`)
- hf auth login --token <EL_TEUTOKEN>
- o exporta HUGGINGFACE_HUB_TOKEN per als scripts

---

## 🛠️ Ús bàsic (scripts reals a la repo)

1) Descarregar un model (text o imatge)
- Text/LLM: python setup/download_model.py <NOM_DEL_MODEL>
  - Exemple: python setup/download_model.py openai-community/gpt2
  - Punt d'entrada: la funció [`download_model`](setup/download_model.py)

- Diffusers (imatge): python setup/download_text_to_image_model.py <NOM_MODEL_IMATGE>
  - Punt d'entrada: [`download_image_model`](setup/download_text_to_image_model.py)

2) Generar una imatge de mostra
- python images/create_sample_image.py
  - Nota: la versió actual no processa flags `--prompt/--output`; modifica [images/create_sample_image.py](images/create_sample_image.py) si necessites paràmetres CLI.

3) Executar proves/guardrails locals
- Auditar prompts (deprecated a /audit_images/deprecated però disponible): python audit_images/deprecated/prompt_guardrail.py "El teu prompt"
- Escaneig d'imatge: python audit_images/probes.py <MODEL_ID>

4) Executar Garak localment amb un snapshot descarregat:
- ./run_garak.sh <Model_ID> [Probes]
  - Exemple: ./run_garak.sh Qwen/Qwen3-0.6B "test.Test"
  - El script localitza el model a `models_cache/` i executa `garak` (veure [run_garak.sh](run_garak.sh)).

5) Batches i escaneigs automatitzats
- [ttt_batch_smokes_scan.sh](ttt_batch_smokes_scan.sh), [ttt_batch_test_scan.sh](ttt_batch_test_scan.sh), [ttimages_batch_smokes_scan.sh](ttimages_batch_smokes_scan.sh)

6) Agregació de resultats
- python utils/aggregate_results.py <nom_model>
  - Implementació: [`utils/aggregate_results.py`](utils/aggregate_results.py)

---

## 🔐 Guardrails i criteris de seguretat
- S'avaluen prompts abans de generar i el contingut resultant (NSFW, hate, divulgació d'informació privada, etc.).
- Les proves actuals són heurístiques simples (paraules clau, heurístiques del pipeline); per producció recomanem integrar models/classificadors especialitzats.

---

## 🔄 Integració amb Jenkins (CI/CD)
Aquest repo inclou Jenkinsfiles preparats:
- [JenkinsfileText](JenkinsfileText) — pipeline per a proves de text
- [JenkinsfileImages](JenkinsfileImages) — pipeline per a flux d'imatges
- [JenkinsGarakSmoke](JenkinsGarakSmoke) i [JenkinsGarakTest](JenkinsGarakTest) — variants amb Garak

Notes: els Jenkinsfiles mostren com crear `venv`, autenticar a Hugging Face i executar els scripts. Ajusta paràmetres de job: `MODELS`, `PROBES`, credencials segures.

---

## 🧪 Probes per al Smoke Test (exemples)
Probes d'exemple (veure [smoke_list_probes.txt](smoke_list_probes.txt) i `ttt_batch_smokes_scan.sh`):
- `dan.DAN_Jailbreak`, `encoding.InjectBase64`, `promptinject.HijackHateHumansMini`, `realtoxicityprompts.RTPInsult`, `packagehallucination.Python`, `xss.MarkdownImageExfil`, etc.

Exemple d'execució Garak:
- python3 -m garak --model_type huggingface --model_name openai-community/gpt2 --probes dan.DAN_Jailbreak,encoding.InjectBase64,packagehallucination.Python

Per integració local i llista completa de probes, usa [run_garak.sh](run_garak.sh) i [smoke_list_probes.txt](smoke_list_probes.txt).

---

## Models sota anàlisi (llista d'exemple)
- `openai-community/gpt2`
- `Qwen/Qwen3-0.6B`
- `Gensyn/Qwen2.5-0.5B-Instruct`
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- `meta-llama/Llama-3.2-1B-Instruct`
- `distilbert/distilgpt2`
- `google/gemma-3-1b-it`

També hi ha models d'imatge a [models.txt](models.txt).

---

## 📐 Bones pràctiques i consells
- Mantén una suite de prompts de prova: segurs, borderline i prohibits.
- Desa logs i informes JSON/HTML per traçabilitat.
- Versiona models i dependències (commit/revision a Hugging Face) per reproductibilitat.

---

## 🤝 Contribució
PRs benvingudes. Obre una issue per a canvis majors. Inclou exemples i tests mínims per a nous guardrails.

---

## 📄 Llicència i autoria
Codi creat per Guillem Hernández Sola. Consulta el repositori per la llicència i autoria.

...existing code...

## 📄 Llicència i autoria
Aquest codi és alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional (CC BY-NC 4.0).  

El README ha estat redactat per a aquest repositori i segueix la mateixa llicència.

Per a més informació o contacte, consulta el perfil de l’autor al repositori.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).