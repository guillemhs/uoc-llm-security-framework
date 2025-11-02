import sys
from PIL import Image
import pytesseract

def check_image_for_guardrails(image_path):
    try:
        # Carrega la imatge des del camí indicat
        image = Image.open(image_path)
    except Exception as e:
        print(f"Error obrint la imatge: {e}")
        sys.exit(2)

    # Extreu el text de la imatge utilitzant OCR
    text = pytesseract.image_to_string(image)
    print(f"Text OCR trobat:\n{text}")

    # Defineix les frases prohibides
    forbidden_phrases = [
        "ignore previous instructions",
        # Pots afegir més frases aquí si cal
    ]

    # Comprova si alguna frase prohibida apareix al text extret
    for phrase in forbidden_phrases:
        if phrase.lower() in text.lower():
            print(f"Guardrail activat! Frase prohibida detectada: '{phrase}'")
            sys.exit(1)

    print("No s'han detectat violacions de guardrails.")
    sys.exit(0)

if __name__ == "__main__":
    # Comprova que s'ha passat el camí de la imatge com a argument
    if len(sys.argv) < 2:
        print("Ús: python image_guardrail.py <camí_imatge>")
        sys.exit(2)
    image_path = sys.argv[1]
    check_image_for_guardrails(image_path)