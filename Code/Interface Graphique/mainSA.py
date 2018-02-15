# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 409)
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
        #print(self.scrollArea.widget())

    def buttonClicked_newAnalyse(self):
        print("nouvelle annalyse")

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

        self.label_etape1.setObjectName("label_etape1")
        self.gridLayout_3.addWidget(self.label_etape1, 0, 0, 1, 3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.label_etape1.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 1 sur 3</span></p></body></html>")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>"))
        self.pushButton_acceuil.setText(_translate("MainWindow", "Acceuil"))
        self.pushButton_newAnalyse.setText(_translate("MainWindow", "Nouvelle analyse"))
        self.pushButton_oldAnalise.setText(_translate("MainWindow", "Charger une analyse"))
        self.pushButton_resultat.setText(_translate("MainWindow", "Résultats"))
        self.pushButton_author.setText(_translate("MainWindow", "About - Author"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
