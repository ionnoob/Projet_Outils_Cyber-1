import string

alphabet = string.ascii_uppercase
size = len(alphabet)

vigenere_matrix = []


for i in range(size):
    row = alphabet[i:] + alphabet[:i]  # Décale tout l'alphabet de 1
vigenere_matrix.append(list(row))


# Décomment pour tester program
# for r in vigenere_matrix[:10]:
#     print(" ".join(r))