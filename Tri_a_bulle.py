# Exercice 2 : Tri à bulles (Bubble Sort)
# Énoncé :
# Écris une fonction tri_bulle(liste) qui prend en paramètre une liste d’entiers non triée, et la trie sur place (sans créer une nouvelle liste),
#  en utilisant la méthode du tri à bulles.

# Contraintes :
#     •    Ton code doit comparer les éléments deux à deux et les échanger si nécessaire.
#     •    Tu dois effectuer plusieurs passages dans la liste, jusqu’à ce qu’il n’y ait plus d’échanges à faire.
#     •    Bonus : optimise le tri en réduisant la zone à trier à chaque passage.


liste = [5, 1, 4, 2, 8]
liste_trie=[]

longueur_liste = len(liste)
print(liste)
print(longueur_liste)

def tribulle(liste):
    longueur_liste = len(liste)
    for i in range(longueur_liste):
        echange_fait = False
        for j in range (0,longueur_liste -i -1):
            if liste[j] > liste [j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echange_fait = True
        if not echange_fait:
            break
        
print (tribulle(liste))


        