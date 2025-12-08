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
