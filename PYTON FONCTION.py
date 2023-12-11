def trier(tableau):
    n = len(tableau)
    for i in range(n - 1):
        # Trouver l'indice du plus grand élément dans la partie non triée
        _max = i
        for j in range(i + 1, n):
            if tableau[j] > tableau[_max]:
                _max = j
        # Échanger l'élément trouvé avec le premier élément non trié
        tableau[i], tableau[_max] = tableau[_max], tableau[i]
    return tableau
def afficher(tableau):
    print("Tableau trié dans l'ordre décroissant : ")
    for i in range(len(tableau)):
        print(tableau[i])
# Exemple d'utilisation 
mon_tableau = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
tableau_trie = trier(mon_tableau)  # Utilisez copy pour ne pas modifier l'original
afficher(tableau_trie)
def ajouter(nom, prenom, tel, type_contact):
    # Ouvrir le fichier en mode append (ajout)
    files = open(r'C:\Users\s3143\OneDrive\Desktop\vecteur\contacts.txt', 'a')
        # Écrire les données du contact dans le fichier
    files.write(f'{nom};{prenom};{tel};{type_contact}\n')

def supprimer_contacts_personnels():
    # Lire le contenu du fichier
    files = open(r'C:\Users\s3143\OneDrive\Desktop\vecteur\contacts.txt', 'r')
    lignes = files.readlines()
    # Réécrire le fichier avec les contacts restants
    files = open(r'C:\Users\s3143\OneDrive\Desktop\vecteur\contacts.txt', 'w')
    files.writelines(ligne for ligne in lignes if not ligne.endswith('personnel\n'))
# Exemple d'utilisation
# Ajouter un contact
ajouter('sem', 'mechil', '1234567890', 'professionnel')
ajouter('smill', 'Jan', '9876543210', 'professionnel')
# Ajouter un contact de type personnel
ajouter('Smi', 'Jite', '9876543211', 'personnel')
# Supprimer les contacts personnels
supprimer_contacts_personnels()
