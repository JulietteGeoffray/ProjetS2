# -*- coding: utf-8 -*-

# Classe permettant le remplisage du fichier de config nécéssaire au lancement du pipeline
# Dans un premier temps tout les champs sont stocké dans un dictionnaire
# Puis le fichier texte est créer avec des vérification des champs.

import datetime

class Formulaire():
    def __init__(self):
        #Dossier des fichier de config -> nom ajouter au moment du nexte de la première page du formulaire
        self.fichier=""
        self.dico = {}
        self.listeChamps=["nom","genRef","plateforme","sample","dbSNPbool","library","rgid","rgpu","backStrainId","mappStrainId", "referenced"]
        for clef in self.listeChamps:
            self.dico[clef]=""

    def etape1(self, genRef, nbrRead, listRead, nom):
        self.dico["genRef"]=genRef.strip("\n").strip(" ")
        self.dico["nbrRead"]=nbrRead
        self.dico["nom"]=str(nom).strip("\n").strip(" ")
        self.fichier=nom
        self.fichier+="_config.py"

        for i in range(len(listRead)):
            read="read"
            read+=str(i)
            self.dico[read]=listRead[i].strip("\n").strip(" ")

    def etape2(self, plateforme, sample, Library, rgid, rgpu):
        self.dico["plateforme"]=plateforme.strip("\n").strip(" ")
        self.dico["sample"]=sample.strip("\n").strip(" ")
        self.dico["library"]=Library.strip("\n").strip(" ")
        self.dico["rgid"]=rgid.strip("\n").strip(" ")
        self.dico["rgpu"]=rgpu.strip("\n").strip(" ")

    def etape3(self,backStrainID, Referenced, MappStrainId, dbsnp, dbSNPbool):
        self.dico["backStrainId"]=backStrainID.strip("\n").strip(" ")
        self.dico["referenced"]=Referenced
        self.dico["dbSNPbool"]=dbSNPbool
        self.dico["mappStrainId"]=MappStrainId.strip("\n").strip(" ")
        self.dico["dbSNP"]=dbsnp.strip("\n").strip(" ")

    def etape4(self, listScaff, InvarScaf, warnScaf):
        self.dico["listScaff"]=listScaff.strip("\n").strip(" ")
        self.dico["InvarScaf"]=InvarScaf.strip("\n").strip(" ")
        self.dico["warnScaf"]=warnScaf.strip("\n").strip(" ")

    def setFichier(self, fichier):
        self.fichier=fichier

    def remplisConfig(self):
        fic="/home/etudiant/Cours/M1S2/Projet/ProjetS2/FichierConfig/"
        fic+=self.fichier
        with open(fic, "w") as fichier_sortie:
            for clef in self.dico:
                s=clef
                s+="="
                s+=str(self.dico[clef])
                s+="\n"
                fichier_sortie.write(s)

    def remplisDico(self, fichier):
        with open(fichier, "r") as fichier_sortie:
            ligne=fichier_sortie.readline()
            while ligne != "":
                ligne=ligne.split("=")
                self.dico[ligne[0]]=ligne[1]
                ligne=fichier_sortie.readline()
