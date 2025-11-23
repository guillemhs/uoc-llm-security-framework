import sys
import subprocess
import shutil
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Ús: python run_garak.py <model_id> [opcions_garak...]")
        print('Exemple: python run_garak.py "openai-community/gpt2" --plugins basics --iterations 50')
        sys.exit(1)

    model_id = sys.argv[1]
    extra_args = sys.argv[2:]  # opcional: flags addicionals per a Garak

    # Verifica que 'garak' està instal·lat i al PATH
    if shutil.which("garak") is None:
        print("Error: No s'ha trobat 'garak' al PATH. Instal·la'l: pip install garak")
        sys.exit(1)

    # Fitxers de sortida
    output_json = Path("resultats_garak.json")
    output_log = Path("resultats_garak.log")

    # Comanda base
    comanda = [
        "garak",
        "--model_name", f"huggingface/{model_id}",
        # Algunes opcions útils per defecte (les pots canviar o eliminar)
    ]

    # Afegeix qualsevol opció extra que passis per línia de comandes
    comanda += extra_args

    print("Executant:", " ".join(comanda))

    try:
        resultat = subprocess.run(
            comanda,
            capture_output=True,
            text=True,
            timeout=3600  # 1 hora; ajusta segons mida del model/proves
        )
    except subprocess.TimeoutExpired:
        print("Temps excedit: Garak ha trigat massa. Augmenta el timeout o redueix proves.")
        sys.exit(124)

    # Desa stdout/stderr a un log per facilitar depuració
    output_log.write_text(
        "=== STDOUT ===\n" + resultat.stdout + "\n\n=== STDERR ===\n" + resultat.stderr
    )

    # Mostra resum a consola
    print("Sortida Garak (resum):")
    print(resultat.stdout[-2000:] if len(resultat.stdout) > 2000 else resultat.stdout)

    if resultat.returncode != 0:
        print("Errors Garak:")
        print(resultat.stderr)
        print(f"Garak ha sortit amb codi {resultat.returncode}. Consulta {output_log} per detalls.")
        sys.exit(resultat.returncode)

    print(f"Anàlisi Garak completada. Resultats desats a {output_json} i log a {output_log}")

if __name__ == "__main__":
    main()