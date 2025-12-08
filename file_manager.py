# --- FILE_MANAGER.PY : version uniquement expliquée en commentaires ---



# OBJECTIF :
# Gérer la lecture et l’écriture de fichiers pour chiffrer/déchiffrer :
# - lire un fichier texte donné par l'utilisateur
# - sauvegarder un texte chiffré ou déchiffré dans un nouveau fichier
# - vérifier que les fichiers existent
# - gérer les erreurs proprement


# 1. Avoir une fonction qui lit un fichier en entrée.
#    Cette fonction doit :
#       - recevoir un nom de fichier
#       - vérifier que le fichier existe
#       - ouvrir le fichier en mode lecture
#       - lire tout son contenu (texte brut)
#       - retourner ce contenu à l'appelant
#    Elle doit aussi gérer les cas :
#       - fichier introuvable
#       - permission refusée
#       - fichier vide


# 2. Avoir une fonction qui écrit un texte dans un fichier de sortie.
#    Cette fonction doit :
#       - recevoir le nom du fichier cible
#       - recevoir le texte à écrire
#       - ouvrir (ou créer) le fichier en mode écriture
#       - sauvegarder le texte dedans
#       - confirmer que l'écriture s’est bien passée
#    Elle doit aussi gérer les problèmes possibles :
#       - impossible de créer le fichier
#       - permissions d’écriture refusées


# 3. Avoir une fonction qui demande à l’utilisateur un chemin de fichier.
#    Cette fonction sert à :
#       - demander où se trouve le fichier à chiffrer ou déchiffrer
#       - vérifier que l'utilisateur n'entre pas un chemin vide
#       - éventuellement vérifier que l’extension est correcte (.txt)
#       - retourner ce chemin


# 4. Avoir une fonction utilitaire pour vérifier si un fichier existe.
#    Elle doit :
#       - prendre un chemin de fichier
#       - utiliser une vérification simple (dans un vrai code : os.path.exists)
#       - retourner True si le fichier est présent, False sinon
#    Et si le fichier n’existe pas :
#       - afficher un message clair à l’utilisateur
#       - empêcher le programme de planter


# 5. Optionnel : une fonction "save_as".
#    Cette fonction :
#       - propose un nom par défaut (ex: "output.txt")
#       - permet à l'utilisateur d’en choisir un autre
#
