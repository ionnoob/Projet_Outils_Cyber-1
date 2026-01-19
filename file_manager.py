# Importation du module os pour pouvoir vérifier l’existence des fichiers
import os



def read_file(filename): # Fonction de lecture d’un fichier texte
    """
    Lis le fichier et le renvoie comme stdout

    """


    # On vérifie d’abord que le fichier existe
    if not os.path.exists(filename):
        # Si le fichier n’existe pas, on affiche un message clair
        raise FileNotFoundError("Erreur : le fichier est introuvable.")
    
    try:
        # Ouverture du fichier en mode lecture texte
        with open(filename, "r", encoding="utf-8") as file:
            # Lecture complète du contenu du fichier
            content = file.read()
            
            # Vérification si le fichier est vide
            if content == "":
                raise ValueError("Erreur : le fichier est vide.")
            
            # Si tout s’est bien passé, on retourne le contenu
            return content

    except PermissionError:
        # Cas où l’utilisateur n’a pas les droits de lecture
        raise PermissionError("Erreur : permission refusée pour lire le fichier.")




def write_file(filename, text): # Fonction d’écriture dans un fichier texte
    """
    Ecrit le contenue dans un fichier

    """


    try:
        # Ouverture (ou création) du fichier en mode écriture
        with open(filename, "w", encoding="utf-8") as file:
            # Écriture du texte dans le fichier
            file.write(text)
        
        # Message de confirmation si l’écriture a réussi
        print(f"Fichier enregistré avec succès : {filename}")

    except PermissionError:
        # Cas où l’écriture n’est pas autorisée
        raise PermissionError("Erreur : permission refusée pour écrire dans le fichier.")

    except OSError:
        # Cas générique : fichier impossible à créer ou autre erreur système
        raise OSError("Erreur : impossible de créer ou d’écrire le fichier.")



def ask_file_path():
    """
    Autorise a l'utilisateur le file path
    """
    
    while True:

        # Demande du chemin à l’utilisateur
        path = input("Entrez le chemin du fichier texte (.txt) : ").strip()
        
        # Vérification que l’entrée n’est pas vide
        if path == "":
            print("Erreur : le chemin ne peut pas être vide.")
            continue
        
        # Vérification de l’extension du fichier
        if not path.lower().endswith(".txt"):
            print("Erreur : le fichier doit avoir l’extension .txt.")
            continue
        
        # Si tout est correct, on retourne le chemin
        return path



def file_exists(path):
    """
    verifie si fichier existe
    """
    
    # Vérification simple de l’existence du fichier
    if os.path.exists(path):
        return True
    else:
        # Message clair si le fichier n’existe pas
        print("Erreur : le fichier spécifié n’existe pas.")
        return False



def save_as(default_name="output.txt"):
    """
    Autorise à l'utilisateur de chosire le nom d'un fichier(utiliser dans le write)
    """
    
    # Affichage de la proposition à l’utilisateur
    print(f"Nom de fichier par défaut : {default_name}")
    
    # Demande d’un autre nom si souhaité
    new_name = input("Entrez un autre nom ou appuyez sur Entrée : ").strip()
    
    # Si l’utilisateur n’entre rien, on garde le nom par défaut
    if new_name == "":
        return default_name
    
    # Sinon, on retourne le nom choisi
    return new_name



def save_key_to_file(key, default_name="key.txt"):
    """
    Sauvegarde la clé a un fichier
    """
    
    # Proposition d’un nom de fichier par défaut
    print(f"Nom de fichier de clé par défaut : {default_name}")
    
    # Demande à l’utilisateur s’il veut un autre nom
    filename = input("Entrez un autre nom ou appuyez sur Entrée : ").strip()
    
    # Si aucun nom n’est donné, on utilise le nom par défaut
    if filename == "":
        filename = default_name
    
    try:
        # Création / écriture du fichier contenant la clé
        with open(filename, "w", encoding="utf-8") as file:
            file.write(key)
        
        # Confirmation de sauvegarde
        print(f"Clé sauvegardée avec succès dans : {filename}")

    except PermissionError:
        # Cas où l’écriture est interdite
        raise PermissionError("Erreur : permission refusée pour écrire la clé.")

    except OSError:
        # Autres erreurs possibles
        raise OSError("Erreur : impossible de sauvegarder la clé.")



def load_key_from_file():
    """
    Load clé d'un fichier
    """
    
    # Demande du chemin du fichier contenant la clé
    path = ask_file_path()
    
    try:
        # Ouverture du fichier de clé
        with open(path, "r", encoding="utf-8") as file:
            key = file.read().strip()
        
        # Vérification que la clé n’est pas vide
        if key == "":
            raise ValueError("Erreur : le fichier de clé est vide.")
        
        # Retour de la clé chargée
        return key

    except FileNotFoundError:
        raise FileNotFoundError("Erreur : fichier de clé introuvable.")

    except PermissionError:
        raise PermissionError("Erreur : permission refusée pour lire la clé.")
