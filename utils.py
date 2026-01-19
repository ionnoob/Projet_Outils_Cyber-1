import random
from vigenere import create_table_vigenere
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

    for m, k in zip(message, key): # verifie m et k dans un zip de message et key mis dans un tuple grace a zip, chaque élément est comparer l'un a l'autre et mis dans une mini liste
        # Par example si j'ai le message : "Hello" et la clé : "ZEFDS" alors mon output est : "(H,Z),(e,E),(F,l),(D,l),(o,S)"

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





def decrypt(ciphertext, key, table):
    """
    Décrypt un message crypté avvec vigenère, tout en conservant
    la ponctuation utilisant la même logique que le chiffrement
    """
    decrypted = ""

    for c,k in zip(ciphertext, key):
        if handle_non_letters(c):
            decrypted+=c
            continue
    
        row = table[k.upper()]
        col = row.index(c.upper())
    

        decrypted_char = alphabet[col]

        if c.islower():
            decrypted_char = decrypted_char.lower()
        decrypted += decrypted_char


    return decrypted







# 
# Usage pour test, a commenter ou décommenter plus tard
# 
#if __name__ == "__main__":
#    message = input("Entre mot a encrypt : ")

    # Create a table of size 26 (A–Z)
#    table = create_table_vigenere()


#    gclé=input("veux-tu générer un clé ou la choisire toi même? Entrer rien pour générer la clé, quelquechose si vous voulez la générer vous même :  ")
 #   if len(gclé)>0: #Si clé est pas nul alors clé générer par utilisateur
  #      key = input("Entrer votre clé en Majuscule: ")
   #     ciphertext = encrypt(message, key, table)

    #    print("Message:     ", message)
     #   print("Key:         ", key)
      #  print("Ciphertext:  ", ciphertext)
    #else: #iSi clé est nul alors génération automatique de la clé
     #   key = generate_random_key(message)
      #  ciphertext = encrypt(message, key, table)

       # print("Message:     ", message)
        #print("Key:         ", key)
        #print("Ciphertext:  ", ciphertext)
