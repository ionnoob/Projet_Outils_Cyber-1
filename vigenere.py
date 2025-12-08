alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def create_table_vigenere():

    table = {}

    for i, lettre_cle in enumerate(alphabet):
        ligne_decalee = alphabet[i:] + alphabet[:i]
        table[lettre_cle] = ligne_decalee

    return table

