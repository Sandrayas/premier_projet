#Un docker est entre un environnement virtuel et une machine virtuelle ? 
#On peut trouver sur le site docker hub une image 
#et on va se servir de cette image 
#on est obligé de passer obligatoirement de passer par une image dans le docker 
#car les images docker permettent detre utilisées en s adaptant a l OS 
#pour que le code puisse fonctionner partout et pour 
#ne pas qu il y ait derreurs si jamais on change d ordi 


#ici on se base sur les images du docker
FROM ubuntu:latest 
#et on choisis de run les commandes suivantes sur ubuntu 
#a partir de là c est comme si on partait d un ordi qui n arien dessus 
RUN apt-get update 

RUN apt-get install python3 -y #-y pour dire yes automatiquement 

RUN apt-get install python3-pip -y

WORKDIR /home

#copie des fichiers dans le docker 
COPY . . 

RUN pip install -r requirements.txt
#cette ligne est equivalente àla commande : python3 main.py 
CMD ["python3", "main.py"]

#on execute ce fichier avec : 
#docker build -t valid_password
#et ensuite on pourra voir les images docker qui se sont creees 
#en tapant docker images
#apres on peut tester une des fonctions du main avec la commande
#docker run valid_password













