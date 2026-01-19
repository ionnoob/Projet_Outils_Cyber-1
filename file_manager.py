import os

OUTPUT_DIR = "Output"

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)


def _full_path(filename):
    ensure_output_dir()
    return os.path.join(OUTPUT_DIR, filename)


def read_file(filename):
    path = _full_path(filename)

    if not os.path.exists(path):
        raise FileNotFoundError(f"Erreur : le fichier est introuvable : {path}")

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

            if content == "":
                raise ValueError("Erreur : le fichier est vide.")

            return content

    except PermissionError:
        raise PermissionError("Erreur : permission refusée pour lire le fichier.")


def write_file(filename, text):
    path = _full_path(filename)

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(text)

        print(f"Fichier enregistré avec succès : {path}")

    except PermissionError:
        raise PermissionError("Erreur : permission refusée pour écrire dans le fichier.")

    except OSError:
        raise OSError("Erreur : impossible de créer ou d’écrire le fichier.")


def ask_file_path():
    while True:
        name = input("Entrez le nom du fichier (.txt) : ").strip()

        if name == "":
            print("Erreur : le nom ne peut pas être vide.")
            continue

        if not name.lower().endswith(".txt"):
            print("Erreur : le fichier doit avoir l’extension .txt.")
            continue

        return name


def save_as(default_name="output.txt"):
    print(f"Nom de fichier par défaut : {default_name}")

    new_name = input("Entrez un autre nom ou appuyez sur Entrée : ").strip()

    if new_name == "":
        return default_name

    return new_name


def save_key_to_file(key, default_name="key.txt"):
    ensure_output_dir()

    print(f"Nom de fichier de clé par défaut : {default_name}")

    filename = input("Entrez un autre nom ou appuyez sur Entrée : ").strip()

    if filename == "":
        filename = default_name

    path = _full_path(filename)

    try:
        with open(path, "w", encoding="utf-8") as file:
            file.write(key)

        print(f"Clé sauvegardée avec succès dans : {path}")

    except PermissionError:
        raise PermissionError("Erreur : permission refusée pour écrire la clé.")

    except OSError:
        raise OSError("Erreur : impossible de sauvegarder la clé.")


def load_key_from_file():
    filename = ask_file_path()
    path = _full_path(filename)

    try:
        with open(path, "r", encoding="utf-8") as file:
            key = file.read().strip()

        if key == "":
            raise ValueError("Erreur : le fichier de clé est vide.")

        return key

    except FileNotFoundError:
        raise FileNotFoundError(f"Erreur : fichier de clé introuvable : {path}")

    except PermissionError:
        raise PermissionError("Erreur : permission refusée pour lire la clé.")
