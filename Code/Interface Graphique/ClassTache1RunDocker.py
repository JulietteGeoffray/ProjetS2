#Clas qui permet de réaliser le lancement de l'analyse via le docker.

import threading
import time
import subprocess
from PyQt5.QtCore import QProcess


class RunDocker (threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)  # ne pas oublier cette ligne
        # (appel au constructeur de la classe mère)
        self.etat = False

    def run(self):
        command = "docker"
        args =  ['run', '-ite', 'DISPLAY', '-v', '/home/etudiant/Bureau/Projet/ProjetS2/testDocker:/home/etudiant/Bureau/Projet/ProjetS2/testDocker', '--net=host', 'essai']
        process = QProcess()
        process.startDetached(command, args)
