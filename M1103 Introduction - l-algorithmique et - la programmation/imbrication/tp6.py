#QUESTION : La météo d'une journée est définie par :

#la température maximale relevée (°C),

#la température minimale relevée (°C),

#la précipitation relevée (mm),

#l'appréciation de la météo : "météo favorable", "météo idéale", etc.

#On représentera la météo d'une journée sous la forme d'un dictionnaire contenant 4 entrées :

#Tmax (la valeur est un entier)

#Tmin (la valeur est un entier)

#"précipitation" (la valeur est un flottant)

#"appréciation" (la valeur est une chaîne de caractères)

#RÉPONSE : 

meteo5janvier = {
    'tMax' : 0,
    'tMin' : -2,
    'precipitation' : 6.9,
    'appreciation' : "météo très défavorable"
}




#QUESTION 2 :
#En utilisant les informations stockées dans meteo5janvier, afficher la phrase :

#Ce jour-là, il a fait -2 °C au minimum, 0 °C au maximum et il a plu 6.9 mm, quelle météo très défavorable !

#REPONSE : 

print ("ce jour là, il fait " + str(meteo5janvier['tMin']) + " °C au minimum, " + str(meteo5janvier['tMax']) + ' °C au maximum et il a plu ' + str(meteo5janvier['precipitation']) + ' mm, quelle météo ' + meteo5janvier['appreciation'])





#QUESTION 3 :
#Les températures pendant tout un mois peuvent être stockées sous la forme d'un tableau de dictionnaires. Il y a autant de cases dans le tableau qu'il y a de jours dans le mois. Chaque case contient alors un dictionnaire comme dans l'exercice 1.

#Attention : Comme l'indice d'un tableau commence à 0, le  ii ème jour sera stocké dans la case d'indice  i−1i−1 .

#Les données du mois de janvier se trouvent dans le fichier meteo_paris_janvier_2009.json contenu dans le répertoire data.

#Créer la variable janvier contenant les informations de la météo au cours du mois de janvier 2009 à Paris. Pour cela, initialiser la variable avec les informations contenues dans le fichier meteo_paris_janvier_2009.json contenu dans le répertoire data.

#Vérifier ensuite que les informations pour le 5 janvier sont les mêmes que pour l'exercice 1.

#REPONSE :

from json import *

f = open("./data/meteo_paris_janvier_2009.json", 'r')
chaine = f.read()
temp_janvier = loads(chaine)
print(temp_janvier[4])
f.close()





#QUESTION 4:

#Déterminer le nombre de jours pour lequel l'appréciation était : "météo très défavorable".

#REPONSE : 

nbr_jours = 0
i = 0
while i < len(s) :
    if temp_janvier[i]['appréciation'] == "météo très défavorable" :
        nbr_jours += 1
    i += 1

    
print("le nombre de jours pour lesquels l'appréciation était 'météo très défavorable' est :" + str(nbr_jours))





#QUESTION :

#Définir fonction Tmax_mois retournant la température maximum relevée dans le mois. En déterminer la température maximum qu'il a fait au mois de janvier.

#REPONSE :

def tMax_mois (tab_temp) :
    i = 1
    temp_max = tab_temp[0]['Tmax']
    while i < len(tab_temp) :
        if tab_temp[i]['Tmax'] > temp_max :
            temp_max = tab_temp[i]['Tmax']
        i += 1
    return temp_max


# détermination de la température maximale du mois de janvier
print('la température maximale du mois de janvier est :')
print(tMax_mois(temp_janvier))






#QUESTION :

#Les températures pour toute l'année 2009 peuvent être stockées sous la forme d'un dictionnaire contenant 12 entrées : les clés sont les noms des mois ("janvier", "février", etc) et les valeurs sont les tableaux de températures du mois (même format que dans l'exercice 2).

#Les données de l'année 2009 se trouvent dans le fichier meteo_paris_2009.json contenu dans le répertoire data.

#Créer la variable meteo2009 contenant les informations de la météo au cours de l'année 2009 à Paris. Pour cela, initialiser la variable avec les informations contenues dans le fichier meteo_paris_2009.json contenu dans le répertoire data.

#Vérifier ensuite que les informations pour le 5 janvier sont les mêmes que pour l'exercice 1.

#REPONSE :

f= open("./data/meteo_paris_2009.json", 'r')
contenu = f.read()
meteo2009 = loads(contenu)






#QUESTION :

#Déterminer le nombre de jours dans l'année où la météo a été appréciée comme "très défavorable".

#REPONSE :

# définition d'une fonction qui determine le nombre de jours très défavorables dans un mois

def nbr_jours_tres_defav(tab_temp_mois):
    i = 0
    nbr_jours = 0
    while i < len(tab_temp_mois) :
        if tab_temp_mois[i]['appréciation'] == 'météo très défavorable':
            nbr_jours += 1
        i += 1
    return nbr_jours

# définition d'une fonction qui calcule le nombre de jours très défavorables dans une année
def nbr_jours_tres_defav_annee(dico_temp_annee):
    tab = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'novembre', 'décembre']
    i = 0
    nbr_jours = 0
    while i < len(tab) :
        nbr_jours += nbr_jours_tres_defav(dico_temp_annee[tab[i]])
        i += 1
    return nbr_jours


print(nbr_jours_tres_defav_annee(meteo2009))







#QUESTION :
#Déterminer la température maximum relevée durant l'année 2009 (utiliser la fonction définie dans la question 3 de l'exercice 2).

#REPONSE :

def temp_max_annee(dico_annee):
    tab = ['janvier', 'février', 'mars', 'avril', 'mai', 'juin', 'juillet', 'août', 'septembre', 'novembre', 'décembre']
    tMax = tMax_mois(dico_annee['janvier'])
    i = 1
    while i < len(tab) :
        if tMax_mois(dico_annee[tab[i]]) > tMax :
            tMax = tMax_mois(dico_annee[tab[i]])
        i += 1
    return tMax

print(temp_max_annee(meteo2009))



