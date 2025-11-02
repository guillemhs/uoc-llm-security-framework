# guardrails/prompt_guardrail.py

import sys

def check_prompt_for_guardrails(prompt):
    # Llista de paraules/frases prohibides
    forbidden_phrases = [
        "ignore previous instructions",
        "disregard all previous prompts",
        "nsfw",
        "offensive",
        # Afegeix aquí tot el que vulguis bloquejar
    ]

    # Comprova si alguna frase prohibida apareix al prompt
    for phrase in forbidden_phrases:
        if phrase.lower() in prompt.lower():
            print(f"Guardrail activat! Frase prohibida detectada al prompt: '{phrase}'")
            sys.exit(1)

    print("Prompt validat: no s'han detectat violacions.")
    sys.exit(0)

if __name__ == "__main__":
    # Comprova que s'ha passat el prompt com a argument
    if len(sys.argv) < 2:
        print("Ús: python prompt_guardrail.py <prompt>")
        sys.exit(2)
    prompt = sys.argv[1]
    check_prompt_for_guardrails(prompt)