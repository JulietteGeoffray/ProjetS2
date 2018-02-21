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
        self.listeChamps=["nom","genRef","plateforme","sample","library","rgid","rgpu","backStrainId","mappStrainId", "referenced"]
        for clef in self.listeChamps:
            self.dico[clef]=""

    def etape1(self, genRef, nbrRead, listRead, nom):
        self.dico["genRef"]=genRef.strip("\n").strip(" ")
        self.dico["nbrRead"]=nbrRead
        self.dico["nom"]=str(nom).strip("\n").strip(" ")
        self.fichier=nom
        self.fichier+=".config"

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

    def etape3(self,backStrainID, Referenced, MappStrainId, dbsnp):
        self.dico["backStrainId"]=backStrainID.strip("\n").strip(" ")
        self.dico["referenced"]=Referenced
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
            date = datetime.datetime.now()
            fichier_sortie.write(str(date))
            fichier_sortie.write("\n\n")
            fichier_sortie.write("-----------Your Input-----------\n")
            fichier_sortie.write("#NomAnalyse :\n{0}\n".format(self.dico["nom"]))
            fichier_sortie.write("#GenRef\n{0}\n".format(self.dico["genRef"]))
            fichier_sortie.write("#Nombre read :\n{0}\n".format(self.dico["nbrRead"]))
            for i in range(self.dico["nbrRead"]):
                read="read"
                read+=str(i)
                fichier_sortie.write("#Read_{0}\n{1}\n".format(i, self.dico[read]))
            fichier_sortie.write("\n")

            fichier_sortie.write("-----------BGI-----------\n")
            fichier_sortie.write("#plateforme :\n{0}\n".format(self.dico["plateforme"]))
            fichier_sortie.write("#sample :\n{0}\n".format(self.dico["sample"]))
            fichier_sortie.write("#library :\n{0}\n".format(self.dico["library"]))
            fichier_sortie.write('#rgid :\n{0}\n'.format(self.dico["rgid"]))
            fichier_sortie.write("#rgpu :\n{0}\n\n".format(self.dico["rgpu"]))

            fichier_sortie.write("-----------population design-----------\n")
            fichier_sortie.write("#backStrainID :\n{0}\n".format(self.dico["backStrainId"]))
            fichier_sortie.write("#referenced :\n{0}\n".format(self.dico["referenced"]))
            fichier_sortie.write("#mappStrainId :\n{0}\n".format(self.dico["mappStrainId"]))
            fichier_sortie.write("#dbSNP :\n{0}\n\n".format(self.dico["dbSNP"]))

            fichier_sortie.write("-----------Additionnal files-----------\n")
            fichier_sortie.write("#ScaffList :\n{0}\n".format(self.dico["listScaff"]))
            fichier_sortie.write('#InvarScaf :\n{0}\n'.format(self.dico["InvarScaf"]))
            fichier_sortie.write("#warnScaf :\n{0}\n\n".format(self.dico["warnScaf"]))

        print("fichier ecrit ok")

    def remplisDico(self, fichier):
        with open(fichier, "r") as fichier_sortie:
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["nom"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["genRef"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["nbrRead"]=ligne
            ligne=fichier_sortie.readline()
            for i in range(int(self.dico["nbrRead"])):
                read="read"
                read+=str(i)
                ligne=fichier_sortie.readline()
                self.dico[read]=ligne
                ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["plateforme"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["sample"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["library"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["rgid"]=ligne
            print(ligne)
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["rgpu"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["backStrainId"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["referenced"]=int(ligne)
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["mappStrainId"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["dbSNP"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["listScaff"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["InvarScaf"]=ligne
            ligne=fichier_sortie.readline()
            ligne=fichier_sortie.readline()
            self.dico["warnScaf"]=ligne
            print(ligne)
