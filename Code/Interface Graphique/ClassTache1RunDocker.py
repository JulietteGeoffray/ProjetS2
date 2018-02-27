#Clas qui permet de réaliser le lancement de l'analyse via le docker.

import threading
import time
import subprocess


class RunDocker (threading.Thread):
    def __init__(self):      # jusqua = donnée supplémentaire
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)
        self.etat = False

    def run(self):
        self.etat = True
        commande="docker run -ite DISPLAY -v /home/etudiant/Bureau/Projet/ProjetS2/testDocker:/home/etudiant/Bureau/Projet/ProjetS2/testDocker --net=host essai"
        sortie = subprocess.Popen(args=commande, stdout=subprocess.PIPE, shell=True)
        TexteSortie=[]
        for line in sortie.stdout:
            TexteSortie.append(str(line.rstrip()).strip("b'").strip("'"))
        self.etat = False
