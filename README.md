# UOC LLM Security Framework

Breu marc de treball per avaluar i integrar bones pràctiques de seguretat en projectes basats en LLM (Large Language Models). Aquest repositori conté eines, guies i exemples per avaluar riscos, aplicar controls i automatitzar proves de seguretat.

## Contingut
- docs/ - Documentació i guies.
- tools/ - Eines d'automatització i scripts.
- examples/ - Exemples i casos de prova.
- tests/ - Suites de proves de seguretat i integritat.
- src/ - Codi font (si escau).

## Característiques
- Llistes de verificació (checklists) per a desplegaments segurs.
- Proves automatitzades per a entrades adverses i fugues d'informació.
- Plantilles de configuració segura per a models i infraestructures.
- Guia de resposta a incidents i mitigacions.

## Requisits
- Python 3.9+ (o l'entorn requerit per a les eines específiques)
- Docker (opcional, per a contenedors i proves reproductibles)
- Clau d'API del model segons les eines que s'utilitzin (no s'inclouen claus en el repositori)

## Instal·lació ràpida
1. Clona el repositori:
   git clone https://github.com/usuari/uoc-llm-security-framework.git
2. Entrar al directori i crear un entorn virtual:
   cd uoc-llm-security-framework
   python -m venv .venv
   source .venv/bin/activate  # ó .venv\Scripts\activate a Windows
3. Instal·lar dependències:
   pip install -r requirements.txt

## Ús
- Revisa la documentació a docs/ per a guies pas a pas.
- Executa les proves de seguretat:
  - scripts/run_security_tests.sh
  - o: pytest tests/
- Adapta les plantilles de configuració a la teva infraestructura abans del desplegament.

## Bones pràctiques recomanades
- No incloure secrets ni claus en el repositori.
- Aplicar controls d'accés i registre (logging) per a totes les consultes als models.
- Validar i filtrar les entrades d'usuari abans d'envair-les al model.
- Revisar resultats i establir límits (rate limits, quotas).

## Contribució
- Llegeix CONTRIBUTING.md (si s'ofereix) i segueix el model de branches i pull requests.
- Obrir issues per a errors o suggeriments.
- Les contribucions haurien d'incloure tests i documentació.

## 📄 Llicència i autoria
Aquest codi és alliberat al domini públic per [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/) sota llicència Creative Commons Reconeixement-NoComercial 4.0 Internacional (CC BY-NC 4.0).  

El README ha estat redactat per a aquest repositori i segueix la mateixa llicència.

Per a més informació o contacte, consulta el perfil de l’autor al repositori.

Si necessiteu més informació, podeu contactar amb [Guillem Hernández Sola](https://www.linkedin.com/in/guillemhs/).

## Contacte
Per dubtes o col·laboració: obre una issue al repositori o contacta amb els mantenidors indicats a la documentació.
