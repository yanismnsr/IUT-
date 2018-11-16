cat /proc/cpuinfo  #commande pour afficher le contenu du fichier cpuinfo qui contient les informations sur le processeur 
grep 'cpu' /proc/cpuinfo #commande qui permet d'afficher les lignes du fichier cpuinfo ou la chaine 'cpu' est présente 
echo "salut">bonjour.out #cette commande ecrase le contenu du fichier bonjour.out pour y remplacer ce que renvoie la commande

echo "Bonjour">>bonjour.out #cette commande n'ecrase pas le contenu du fichier contrairement a la premiere, elle rajoute 
      #directement ce que renvoie la commande au fichier sans éffacer son contenu 


cat /proc/cpuinfo | wc -l  #le pipe (|) sert à renvoyer ce que renvoie la commande précédente dans la commande suivante 

#commande pour afficher le nombre de fichiers dans le repertoire personnel 
ls -l | grep '^-' | wc -l

#comter le nombre de processus dans le systeme 
ps ax | wc -l


#commande pour afficher les 5 premieres lignes des 10 dernieres lignes du fichier /proc/cpuinfo
tail /proc/cpuinfo | head -n 5


#### script qui met dans une variable le contenu du fichier /usr/share/dict/french dans une variable ###
#pour affecter le resultat d'une commande dans une variable, on utilise le $(commande)
a=$(cat /usr/share/dict/french | grep 'cool')




#### script permettant d'afficher chaque mot comportant les caractères "cool", avec a chaque fois devant "ce mot là est cool :" ... suivi du mot en question
a=$(grep 'cool' /usr/share/dict/french)

for i in $a; do
    echo "ce mot la est cool : $i"
done
