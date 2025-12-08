import string

def vinegere_create(s):
    """
    Créé table vignere de la taille de S où s = alphabet
    """
    alphabet = string.ascii_uppercase[:s]
    table = []

    for i in range(s):
        shifted = alphabet[i:] + alphabet[:i]
        table.append(shifted)

    return table
