import random
import string
from vingere.py import create_table_vignere
#import fonction vinegere_create donc a garder les deux fichiers dans le même directoir
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def generate_random_key(message):
    """
    Génere clé de la même taille que le message
    les characters non-alphabetique gardent leur place pour ne pas changer la ponctuation.
    """
    key = ""

    for char in message:
        if char.isalpha(): #si char(chaque element dans le message par itération) est une lettre de l'alphabet
            key += random.choice(alphabet)
        else:
            key += char  # Garde les espaces/ponctuation

    return key


def handle_non_letters(char):
    """Return True si pas lettre alphabetique"""
    return not char.isalpha()


def encrypt(message, key, table):
    """
    passe par chaque lettre pour encrypter avec liste vigenere générer par fonction dans autre fichier
    copie lettre non_alphabetique pour ne pas ruiner ponctuation
    """
    
    encrypted = ""

    for m, k in zip(message, key): #double incrémentation où on verifie chaque m dans message et chaque k dans key

        if handle_non_letters(m): #appel à fonction 
            encrypted += m #rajoute la lettre au message encypter
            continue #continue pour toute les lettres

        row = table[k.upper()] #compare à table vinegere en maj puisque ca doit etre en maj
        col = alphabet.index(m.upper()) #fait la même 
        encrypted_char = row[col] #la clé est utilisé comme row donc, si on a A B C et que k=B alors on prend la colone de B et on déscend en prenant la lettre correspondant a la lettre qu'on encrypt

        # maintient si la lettre est maj ou pas
        if m.islower():
            encrypted_char = encrypted_char.lower()

        encrypted += encrypted_char

    return encrypted


# 
# Usage pour test, a commenter ou décommenter plus tard
# 
if __name__ == "__main__":
    message = input("Entre mot a encrypt : ")

    # Create a table of size 26 (A–Z)
    table = create_table_vigenere()


    gclé=input("veux-tu générer un clé ou la choisire toi même? Entrer rien pour générer la clé, quelquechose si vous voulez la générer vous même :  ")
    if len(gclé)>0: #Si clé est pas nul alors clé générer par utilisateur
        key = input("Entrer votre clé en Majuscule: ")
        ciphertext = encrypt(message, key, table)

        print("Message:     ", message)
        print("Key:         ", key)
        print("Ciphertext:  ", ciphertext)
    else: #iSi clé est nul alors génération automatique de la clé
        key = generate_random_key(message)
        ciphertext = encrypt(message, key, table)

        print("Message:     ", message)
        print("Key:         ", key)
        print("Ciphertext:  ", ciphertext)

# --- Décryptage Vigenère : version préliminaire  ---

# Traite chaque char du texte un par un
# Avance dans la clé en même temps(double incrémentation?)

# 1. Prendre la lettre chiffrée courante.
# 2. Prendre la lettre de la clé correspondante.
# 3. Si ce n’est pas une lettre (espace, virgule, etc.), on la renvoie tel quel.
#    On ne modifie pas la ponctuation ni les espaces.
# 4. Si c’est une lettre, on regarde dans la table Vigenère.
#    dico donc chaque clé est une lettre (A, B, C ...)
#    et la valeur est une ligne de l’alphabet décalée.
# 5. On utilise la lettre de la clé pour choisir la bonne ligne
# 6. Dans cette ligne, on cherche l’index de la lettre chiffrée.
#    index correspond a la position où cette lettre apparaît dans la ligne décalée.
# 7. Avec index, on récupère lettre d’origine dans l’alphabet normal :
# 8. On garde maj pour maj en min pour min
# 9. On ajoute la lettre déchiffrée au résultat final. comme dans le premier code
# 10. On passe au caractère suivant du texte chiffré et on recommence jusqu’à la fin.


