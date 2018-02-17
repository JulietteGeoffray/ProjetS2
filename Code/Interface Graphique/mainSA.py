# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets

import ClassFormulaire

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        ######################################################################
        #                                                                    #
        #         Fenetre princiale (menu gauche + scroll bar area)          #
        #                                                                    #
        ######################################################################

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(0, 344))
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 400))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_titre = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_titre.setFont(font)
        self.label_titre.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_titre.setAcceptDrops(False)
        self.label_titre.setLayoutDirection(QtCore.Qt.LeftToRight)

        self.label_titre.setObjectName("label_titre")
        self.gridLayout_2.addWidget(self.label_titre, 0, 0, 1, 1)
        self.pushButton_acceuil = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_acceuil.setObjectName("pushButton_acceuil")
        self.gridLayout_2.addWidget(self.pushButton_acceuil, 1, 0, 1, 1)
        self.pushButton_newAnalyse = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_newAnalyse.clicked.connect(self.buttonClicked_newAnalyse)

        self.pushButton_newAnalyse.setObjectName("pushButton_newAnalyse")
        self.gridLayout_2.addWidget(self.pushButton_newAnalyse, 2, 0, 1, 1)
        self.pushButton_oldAnalise = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_oldAnalise.setObjectName("pushButton_oldAnalise")
        self.gridLayout_2.addWidget(self.pushButton_oldAnalise, 3, 0, 1, 1)
        self.pushButton_resultat = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_resultat.setObjectName("pushButton_resultat")
        self.gridLayout_2.addWidget(self.pushButton_resultat, 4, 0, 1, 1)
        self.pushButton_author = QtWidgets.QPushButton(self.groupBox_2)

        self.pushButton_author.setObjectName("pushButton_author")
        self.gridLayout_2.addWidget(self.pushButton_author, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 657, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #Signal et connection
        self.pushButton_acceuil.clicked.connect(self.buttonClicked_acceuil)

    def buttonClicked_acceuil(self):
        print("acceuil")

        #Ajout d'un bouton :
        #btn2 = QtWidgets.QPushButton("bouton :)", self.scrollArea)
        #self.scrollArea.setWidget(btn2)
        #nbr = self.scrollArea.widget()

        self.scrollArea.hide()

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        btn2 = QtWidgets.QPushButton("bouton :)", self.scrollArea)
        self.scrollArea.setWidget(btn2)

        ######################################################################
        #                                                                    #
        #                          FORMULAIRE                                #
        #                4 étapes + étape lance l'analyse                    #
        ######################################################################

        ######################################################################
        #               formualire end -> lance l'analyse                    #
        ######################################################################

    def RunAnalysis(self):
        print("Run Analysis")

        # Chope les textes des champs précédant
        listScaff=self.lineEdit_listScaff.text()
        InvarScaf=self.lineEdit_InvarScaf.text()
        warnScaf=self.lineEdit_warnScaf.text()
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        new.etape4(listScaff, InvarScaf, warnScaf)
        print(new.dico)

        

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                      Formulaire - Etape 4                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape4(self):
        print("etape 4 formulaire")

        # Chope les textes des champs précédant
        backStrainID=self.lineEdit_backStrainId.text()
        mappStrainId=self.lineEdit_mappStrainId.text()
        dbSNP=self.lineEdit_dbsnp.text()

        if self.radioButton_yesRef.isChecked():
            referenced=0
        else:
            referenced=1
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        new.etape3(backStrainID, referenced, mappStrainId, dbSNP)
        print(new.dico)

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label_etape4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape4.setObjectName("label_etape4")
        self.label_etape4.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 4 sur 4</span></p></body></html>")

        self.gridLayout_2.addWidget(self.label_etape4, 0, 0, 1, 1)
        self.label_titre4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre4.setObjectName("label_titre4")
        self.label_titre4.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Additionnal files</span></p></body></html>")

        self.gridLayout_2.addWidget(self.label_titre4, 1, 0, 1, 1)

        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")

        self.label_listScaff = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_listScaff.setObjectName("label_listScaff")
        self.label_listScaff.setText("List of scaffolds ID and their size :")

        self.horizontalLayout_18.addWidget(self.label_listScaff)

        self.lineEdit_listScaff = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_listScaff.setText("")
        self.lineEdit_listScaff.setObjectName("lineEdit_listScaff")

        if "listScaff" in new.dico.keys():
            if new.dico["listScaff"] != "":
                self.lineEdit_listScaff.setText(new.dico["listScaff"])

        self.horizontalLayout_18.addWidget(self.lineEdit_listScaff)

        self.toolButton_listScaff = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_listScaff.setObjectName("toolButton_listScaff")
        self.toolButton_listScaff.setText("...")

        self.horizontalLayout_18.addWidget(self.toolButton_listScaff)

        self.gridLayout_2.addLayout(self.horizontalLayout_18, 2, 0, 1, 1)

        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")

        self.label_InvarScaf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_InvarScaf.setObjectName("label_InvarScaf")
        self.label_InvarScaf.setText("\"Invariant\" Scaffolds :                       ")

        self.horizontalLayout_11.addWidget(self.label_InvarScaf)

        self.lineEdit_InvarScaf = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_InvarScaf.setText("")
        self.lineEdit_InvarScaf.setObjectName("lineEdit_InvarScaf")

        if "InvarScaf" in new.dico.keys():
            if new.dico["InvarScaf"] != "":
                self.lineEdit_InvarScaf.setText(new.dico["InvarScaf"])

        self.horizontalLayout_11.addWidget(self.lineEdit_InvarScaf)

        self.toolButton_InvarScaf = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_InvarScaf.setObjectName("toolButton_InvarScaf")
        self.toolButton_InvarScaf.setText("...")

        self.horizontalLayout_11.addWidget(self.toolButton_InvarScaf)

        self.gridLayout_2.addLayout(self.horizontalLayout_11, 3, 0, 1, 1)

        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")

        self.label_17 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_17.setObjectName("label_17")
        self.label_17.setToolTip("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">list of scaffolds you want to test even if they are not linked to your mutation. (e.g. False-positive or so-far-unlinked scaffolds)</span></p></body></html>")
        self.label_17.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")

        self.horizontalLayout_13.addWidget(self.label_17)

        self.label_warnScaf = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_warnScaf.setObjectName("label_warnScaf")

        self.horizontalLayout_13.addWidget(self.label_warnScaf)

        self.lineEdit_warnScaf = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_warnScaf.setText("")
        self.lineEdit_warnScaf.setObjectName("lineEdit_warnScaf")

        if "warnScaf" in new.dico.keys():
            if new.dico["warnScaf"] != "":
                self.lineEdit_warnScaf.setText(new.dico["warnScaf"])

        self.label_warnScaf.setToolTip("<html><head/><body><p><br/></p></body></html>")
        self.label_warnScaf.setText("Warning Scaffolds :                       ")

        self.horizontalLayout_13.addWidget(self.lineEdit_warnScaf)

        self.toolButton_warnScaf = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_warnScaf.setObjectName("toolButton_warnScaf")
        self.toolButton_warnScaf.setText("...")

        self.horizontalLayout_13.addWidget(self.toolButton_warnScaf)

        self.gridLayout_2.addLayout(self.horizontalLayout_13, 4, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_2.addItem(spacerItem, 5, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.pushButton_back4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back4.setObjectName("pushButton_back4")
        self.pushButton_back4.setText("Back")
        self.pushButton_back4.clicked.connect(self.buttonClicked_newAnalyse_etape3)

        self.horizontalLayout.addWidget(self.pushButton_back4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.pushButton_runAnalysis = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_runAnalysis.setMinimumSize(QtCore.QSize(116, 0))
        self.pushButton_runAnalysis.setMaximumSize(QtCore.QSize(50, 30))
        self.pushButton_runAnalysis.setSizeIncrement(QtCore.QSize(1, 1))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(170, 255, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 241, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton_runAnalysis.setPalette(palette)
        self.pushButton_runAnalysis.setObjectName("pushButton_runAnalysis")
        self.pushButton_runAnalysis.setText("Run Analysis")
        self.pushButton_runAnalysis.clicked.connect(self.RunAnalysis)

        # run analis : création du fichier config avec class formulaire
        # si la création du fichier renvoie ok on lance l'analyse
        # sinon on renseigne le champs qui pose probleme et on chance sa valeur
        # nouvelle vérif apres erreur
        # -> dans une fenetre popup
        # Boucle do - jusqu'a ce que ce sois bon puis on lance l'analise

        self.horizontalLayout.addWidget(self.pushButton_runAnalysis)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 1)

        #self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        #self.gridLayout_3.addWidget(self.scrollArea, 0, 1, 1, 1)
        #MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                      Formulaire - Etape 3                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape3(self):
        print("etape 3 formulaire")

        # Chope les textes des champs précédant
        plateforme=self.lineEdit_plateforme.text()
        sample=self.lineEdit_sample.text()
        library=self.lineEdit_library.text()
        rgid=self.lineEdit_rgid.text()
        rgpu=self.lineEdit_rgpu.text()
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        new.etape2(plateforme, sample, library, rgid, rgpu)
        print(new.dico)

        self.scrollArea.hide()
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.label_etape3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape3.setObjectName("label_etape3")
        self.label_etape3.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 3 sur 4</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_etape3, 0, 0, 1, 1)

        self.label_titre3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre3.setObjectName("label_titre3")
        self.label_titre3.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Design of the population for the cartographie</span></p></body></html>")

        self.gridLayout_3.addWidget(self.label_titre3, 1, 0, 1, 1)

        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")

        self.label_backStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_backStrainId.setObjectName("label_backStrainId")
        self.label_backStrainId.setText("Background strain ID  :                       ")

        self.horizontalLayout_10.addWidget(self.label_backStrainId)

        self.lineEdit_backStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_backStrainId.setText("")
        self.lineEdit_backStrainId.setObjectName("lineEdit_backStrainId")

        if "backStrainId" in new.dico.keys():
            if new.dico["backStrainId"] != "":
                self.lineEdit_backStrainId.setText(new.dico["backStrainId"])

        self.horizontalLayout_10.addWidget(self.lineEdit_backStrainId)

        self.gridLayout_3.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_ref = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ref.setObjectName("label_ref")
        self.label_ref.setText("Referenced  :                                                 ")

        self.horizontalLayout.addWidget(self.label_ref)

        self.radioButton_yesRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_yesRef.setObjectName("radioButton_yesRef")
        self.radioButton_yesRef.setText("yes")

        if "referenced" in new.dico.keys():
            if new.dico["referenced"] == 0:
                self.radioButton_yesRef.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_yesRef)

        self.radioButton_noRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_noRef.setObjectName("radioButton_noRef")
        self.radioButton_noRef.setText("no")

        if "referenced" in new.dico.keys():
            if new.dico["referenced"] == 1:
                self.radioButton_noRef.setChecked(True)

        self.horizontalLayout.addWidget(self.radioButton_noRef)

        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)

        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")

        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.label_20.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_20.setToolTip("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">It should be the same as RGSM appearing in the $Mapping_gVCF (determine with &quot;Read Group&quot; information during analysis)</span></p></body></html>")

        self.horizontalLayout_16.addWidget(self.label_20)

        self.label_mappStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_mappStrainId.setObjectName("label_mappStrainId")
        self.label_mappStrainId.setText("Mapping strain ID :                          ")

        self.horizontalLayout_16.addWidget(self.label_mappStrainId)

        self.lineEdit_mappStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_mappStrainId.setText("")
        self.lineEdit_mappStrainId.setObjectName("lineEdit_mappStrainId")

        if "mappStrainId" in new.dico.keys():
            if new.dico["mappStrainId"] != "":
                self.lineEdit_mappStrainId.setText(new.dico["mappStrainId"])

        self.horizontalLayout_16.addWidget(self.lineEdit_mappStrainId)

        self.gridLayout_3.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)

        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")

        self.label_dbsnp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_dbsnp.setObjectName("label_dbsnp")
        self.label_dbsnp.setText("dbSNP (background vs mapping)  :")

        self.horizontalLayout_17.addWidget(self.label_dbsnp)

        self.lineEdit_dbsnp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_dbsnp.setText("")
        self.lineEdit_dbsnp.setObjectName("lineEdit_dbsnp")

        if "dbSNP" in new.dico.keys():
            if new.dico["dbSNP"] != "":
                self.lineEdit_dbsnp.setText(new.dico["dbSNP"])

        self.horizontalLayout_17.addWidget(self.lineEdit_dbsnp)

        self.toolButton_dbsnp = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_dbsnp.setObjectName("toolButton_dbsnp")
        self.toolButton_dbsnp.setText("...")

        self.horizontalLayout_17.addWidget(self.toolButton_dbsnp)

        self.gridLayout_3.addLayout(self.horizontalLayout_17, 5, 0, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.pushButton_back3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back3.setObjectName("pushButton_back3")
        self.pushButton_back3.setText("Back")
        self.pushButton_back3.clicked.connect(self.buttonClicked_newAnalyse_etape2)

        self.horizontalLayout_2.addWidget(self.pushButton_back3)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem1)

        self.pushButton_next3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next3.setObjectName("pushButton_next3")
        self.pushButton_next3.setText("Next")
        self.pushButton_next3.clicked.connect(self.buttonClicked_newAnalyse_etape4)

        self.horizontalLayout_2.addWidget(self.pushButton_next3)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                      Formulaire - Etape 2                          #
        ######################################################################

    def buttonClicked_newAnalyse_etape2(self):
        print("etape 2 formulaire")

        ## Avant de cacher les champs et de les "effacer" je recupere les valeurs des
        ## champs pour remplir le fichier de config
        # Chope les texte
        GenRef=self.lineEdit_GenRef.text()
        read=[]
        read.append(self.lineEdit_Read1.text())
        read.append(self.lineEdit_Read2.text())
        # On les sauvegarde dans le dictionnaire qui gènre les champs
        new.etape1(GenRef, 2, read)
        print(new.dico)

        ## Mise en place des champs de formulaire pour l'affichage de l'étape 2
        # Cacher les ancien champs en cachant la scroll area
        self.scrollArea.hide()
        # Recréer l'esapce de scroll area vide
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        # Ajout de tout les champs dans la nouvelle scroll area de l'etape 2

        self.gridLayout_5 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")

        self.pushButton_next2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next2.setObjectName("pushButton_next2")
        self.pushButton_next2.setText("Next")
        self.pushButton_next2.clicked.connect(self.buttonClicked_newAnalyse_etape3)

        self.gridLayout_4.addWidget(self.pushButton_next2, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem, 0, 1, 1, 1)
        self.pushButton_back2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back2.setObjectName("pushButton_back2")
        self.pushButton_back2.setText("Back")
        self.pushButton_back2.clicked.connect(self.buttonClicked_newAnalyse)

        self.gridLayout_4.addWidget(self.pushButton_back2, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 4, 0, 1, 2)
        self.label_Indiq2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Indiq2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_Indiq2.setObjectName("label_Indiq2")
        self.label_Indiq2.setText("<html><head/><body><p align=\"justify\"><span style=\" font-size:10pt; font-style:italic;\">Les noms des fichiers seront construis ainsi : {FlowCellID}-{sampleID}_Lane </span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_Indiq2, 2, 0, 1, 2)

        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.label_sample = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_sample.setObjectName("label_sample")
        self.label_sample.setText("Sample :         ")

        self.horizontalLayout_2.addWidget(self.label_sample)

        self.lineEdit_sample = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_sample.setObjectName("lineEdit_sample")
        self.lineEdit_sample.setText("")

        if "sample" in new.dico.keys():
            if new.dico["sample"] != "":
                self.lineEdit_sample.setText(new.dico["sample"])

        self.horizontalLayout_2.addWidget(self.lineEdit_sample)

        self.gridLayout_3.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label_library = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_library.setObjectName("label_library")
        self.label_library.setText("Library :          ")

        self.horizontalLayout.addWidget(self.label_library)

        self.lineEdit_library = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_library.setObjectName("lineEdit_library")
        self.lineEdit_library.setText("")

        if "library" in new.dico.keys():
            if new.dico["library"] != "":
                self.lineEdit_library.setText(new.dico["library"])

        self.horizontalLayout.addWidget(self.lineEdit_library)

        self.gridLayout_3.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.label_8.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_8.setToolTip("<html><head/><body><p>Choose \'Flow Cell ID\'_\'sample\'</p></body></html>")

        self.horizontalLayout_5.addWidget(self.label_8)

        self.label_rgid = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_rgid.setObjectName("label_rgid")
        self.label_rgid.setText("RGID :         ")

        self.horizontalLayout_5.addWidget(self.label_rgid)

        self.lineEdit_rgid = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_rgid.setObjectName("lineEdit_rgid")

        if "rgid" in new.dico.keys():
            if new.dico["rgid"] != "":
                self.lineEdit_rgid.setText(new.dico["rgid"])

        self.horizontalLayout_5.addWidget(self.lineEdit_rgid)

        self.gridLayout_3.addLayout(self.horizontalLayout_5, 3, 0, 1, 1)

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")

        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")

        self.label_9.setText("<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">i</span></p></body></html>")
        self.label_9.setToolTip("<html><head/><body><p>Choose \'Flow Cell ID\'_\'Lane\'_\'sample\'</p></body></html>")

        self.horizontalLayout_4.addWidget(self.label_9)

        self.label_rgpu = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_rgpu.setObjectName("label_rgpu")
        self.label_rgpu.setText("RGPU :        ")

        self.horizontalLayout_4.addWidget(self.label_rgpu)

        self.lineEdit_rgpu = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_rgpu.setObjectName("lineEdit_rgpu")

        if "rgpu" in new.dico.keys():
            if new.dico["rgpu"] != "":
                self.lineEdit_rgpu.setText(new.dico["rgpu"])

        self.horizontalLayout_4.addWidget(self.lineEdit_rgpu)

        self.gridLayout_3.addLayout(self.horizontalLayout_4, 4, 0, 1, 1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        self.label_plateforme = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_plateforme.setObjectName("label_plateforme")
        self.label_plateforme.setText("Plateforme : ")

        self.horizontalLayout_3.addWidget(self.label_plateforme)

        self.lineEdit_plateforme = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_plateforme.setObjectName("lineEdit_plateforme")
        self.lineEdit_plateforme.setText("")

        if "plateforme" in new.dico.keys():
            if new.dico["plateforme"] != "":
                self.lineEdit_plateforme.setText(new.dico["plateforme"])

        self.horizontalLayout_3.addWidget(self.lineEdit_plateforme)

        self.gridLayout_3.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.gridLayout_5.addLayout(self.gridLayout_3, 3, 0, 1, 2)

        self.label_BGI = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_BGI.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_BGI.setMidLineWidth(0)
        self.label_BGI.setIndent(1)
        self.label_BGI.setOpenExternalLinks(False)
        self.label_BGI.setObjectName("label_BGI")
        self.label_BGI.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># BGI </span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_BGI, 1, 0, 1, 1)

        self.label_etape2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape2.setObjectName("label_etape2")
        self.label_etape2.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 2 sur 4</span></p></body></html>")

        self.gridLayout_5.addWidget(self.label_etape2, 0, 0, 1, 2)

        self.label_BGI.raise_()
        self.label_Indiq2.raise_()
        self.label_etape2.raise_()

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        ######################################################################
        #                      Formulaire - Etape 1                          #
        ######################################################################

        #if i in self.dico_indexer_read.keys():

    def buttonClicked_newAnalyse(self):
        print("nouvelle annalyse")

        self.scrollArea.hide()

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 342))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_titre = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre.setMaximumSize(QtCore.QSize(16777215, 30))

        self.label_titre.setObjectName("label_titre")
        self.gridLayout_3.addWidget(self.label_titre, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_titre.setText("<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Your inputs :</span></p></body></html>")
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_GenRef = QtWidgets.QLabel(self.scrollAreaWidgetContents)

        self.label_GenRef.setObjectName("label_GenRef")
        self.label_GenRef.setText("Génome de référence :    ")
        self.horizontalLayout_4.addWidget(self.label_GenRef)
        self.lineEdit_GenRef = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)

        self.lineEdit_GenRef.setObjectName("lineEdit_GenRef")
        self.horizontalLayout_4.addWidget(self.lineEdit_GenRef)
        self.toolButton_GenRef = QtWidgets.QToolButton(self.scrollAreaWidgetContents)

        if "genRef" in new.dico.keys():
            if new.dico["genRef"] != "":
                self.lineEdit_GenRef.setText(new.dico["genRef"])

        self.toolButton_GenRef.setObjectName("toolButton_GenRef")
        self.horizontalLayout_4.addWidget(self.toolButton_GenRef)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.toolButton_GenRef.setText("...")

        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Read1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)

        self.label_Read1.setObjectName("label_Read1")
        self.horizontalLayout.addWidget(self.label_Read1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.label_Read1.setText("[1] Séquences des reads :")

        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout.addLayout(self.horizontalLayout_5)

        self.lineEdit_Read1 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Read1.setObjectName("lineEdit_Read1")

        # remplir le champs des read en fonction du nombre
        # A voir plus tard, peut etre en même temps que la gestion
        # d'ajout de 2 - 4 - 8... fichier de reads
        #if "genRef" in new.dico.keys():
        #    if new.dico["genRef"] != "":
        #        self.lineEdit_GenRef.setText(new.dico["genRef"])

        self.horizontalLayout.addWidget(self.lineEdit_Read1)
        self.toolButton_Read1 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)

        self.toolButton_Read1.setObjectName("toolButton_Read1")
        self.horizontalLayout.addWidget(self.toolButton_Read1)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.toolButton_Read1.setText("...")

        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Read2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)

        self.label_Read2.setObjectName("label_Read2")
        self.horizontalLayout_3.addWidget(self.label_Read2)
        self.lineEdit_Read2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.label_Read2.setText("[2] Séquences des reads :")

        self.lineEdit_Read2.setObjectName("lineEdit_Read2")
        self.horizontalLayout_3.addWidget(self.lineEdit_Read2)
        self.toolButton_Read2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)

        self.toolButton_Read2.setObjectName("toolButton_Read2")
        self.horizontalLayout_3.addWidget(self.toolButton_Read2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 3)
        self.pushButton_plus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_plus.setMaximumSize(QtCore.QSize(30, 30))
        self.toolButton_Read2.setText("...")

        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout_3.addWidget(self.pushButton_plus, 5, 1, 1, 1)
        self.pushButton_moins = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_moins.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_plus.setText("+")

        self.pushButton_moins.setObjectName("pushButton_moins")
        self.gridLayout_3.addWidget(self.pushButton_moins, 5, 2, 1, 1)
        self.pushButton_moins.setText("-")

        spacerItem = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(265, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 7, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(265, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem2, 8, 0, 1, 1)
        self.pushButton_next1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)

        self.pushButton_next1.setObjectName("pushButton_next1")
        self.gridLayout_3.addWidget(self.pushButton_next1, 8, 1, 1, 2)
        self.label_etape1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pushButton_next1.setText("Next")
        self.pushButton_next1.clicked.connect(self.buttonClicked_newAnalyse_etape2)

        self.label_etape1.setObjectName("label_etape1")
        self.gridLayout_3.addWidget(self.label_etape1, 0, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_etape1.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 1 sur 4</span></p></body></html>")

    #Fonction qui ajoute le texte sur les éléments de la fenetre princiale (= menu a gauche)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>"))
        self.pushButton_acceuil.setText(_translate("MainWindow", "Accueil"))
        self.pushButton_newAnalyse.setText(_translate("MainWindow", "Nouvelle analyse"))
        self.pushButton_oldAnalise.setText(_translate("MainWindow", "Charger une analyse"))
        self.pushButton_resultat.setText(_translate("MainWindow", "Résultats"))
        self.pushButton_author.setText(_translate("MainWindow", "About - Author"))

        ######################################################################
        #                                                                    #
        #                Boucle principale du programmme                     #
        #                                                                    #
        ######################################################################

if __name__ == "__main__":
    import sys
    new=ClassFormulaire.Formulaire()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
