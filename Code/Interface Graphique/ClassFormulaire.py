# -*- coding: utf-8 -*-

# Classe permettant le remplisage du fichier de config nécéssaire au lancement du pipeline
# Dans un premier temps tout les champs sont stocké dans un dictionnaire
# Puis le fichier texte est créer avec des vérification des champs.

class Formulaire():
    def __init__(self):
        self.fichier=""
        self.dico = {}
        self.listeChamps=["genRef","plateforme","sample","library","rgid","rgpu","backStrainId","mappStrainId","warnScaf", "referenced"]
        for clef in self.listeChamps:
            self.dico[clef]=""


    def etape1(self, genRef, nbrRead, listRead):
        self.dico["genRef"]=genRef
        self.dico["nbrRead"]=nbrRead
        for i in range(nbrRead):
            read="read"
            read+=str(i)
            self.dico[read]=listRead[i]

    def etape2(self, plateforme, sample, Library, rgid, rgpu):
        self.dico["plateforme"]=plateforme
        self.dico["sample"]=sample
        self.dico["library"]=Library
        self.dico["rgid"]=rgid
        self.dico["rgpu"]=rgpu

    def etape3(self,backStrainID, Referenced, MappStrainId, dbsnp):
        self.dico["backStrainId"]=backStrainID
        self.dico["referenced"]=Referenced
        self.dico["mappStrainId"]=MappStrainId
        self.dico["dbSNP"]=dbsnp

    def etape4(self, listScaff, InvarScaf, warnScaf):
        self.dico["listScaff"]=listScaff
        self.dico["InvarScaf"]=InvarScaf
        self.dico["warnScaf"]=warnScaf

    def setFichier(self, fichier):
        self.fichier=fichier

    def remplisConfig(self):
        pass
