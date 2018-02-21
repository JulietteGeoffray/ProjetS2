# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainErreurForm.ui'
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
        self.pushButton_newAnalyse = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_newAnalyse.setObjectName("pushButton_newAnalyse")
        self.gridLayout_2.addWidget(self.pushButton_newAnalyse, 2, 0, 1, 1)
        self.pushButton_acceuil = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_acceuil.setObjectName("pushButton_acceuil")
        self.gridLayout_2.addWidget(self.pushButton_acceuil, 1, 0, 1, 1)
        self.pushButton_resultat = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_resultat.setObjectName("pushButton_resultat")
        self.gridLayout_2.addWidget(self.pushButton_resultat, 4, 0, 1, 1)
        self.pushButton_oldAnalise = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_oldAnalise.setObjectName("pushButton_oldAnalise")
        self.gridLayout_2.addWidget(self.pushButton_oldAnalise, 3, 0, 1, 1)
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


        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setMaximumSize(QtCore.QSize(80, 70))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../../../../../../../Cours/M1S2/Projet/ProjetS2/sign-warning-icon.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout_4.addLayout(self.horizontalLayout, 2, 0, 2, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_3.addWidget(self.pushButton, 0, 1, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem1, 0, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(356, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 1, 0, 1, 2)
        spacerItem3 = QtWidgets.QSpacerItem(350, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem3, 4, 1, 1, 1)
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

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>"))
        self.pushButton_newAnalyse.setText(_translate("MainWindow", "Nouvelle analyse"))
        self.pushButton_acceuil.setText(_translate("MainWindow", "Acceuil"))
        self.pushButton_resultat.setText(_translate("MainWindow", "Résultats"))
        self.pushButton_oldAnalise.setText(_translate("MainWindow", "Charger une analyse"))
        self.pushButton_author.setText(_translate("MainWindow", "About - Author"))
        self.label_2.setText(_translate("MainWindow", "This information are rong : \n"
"\n"
"- Génome de référence"))
        self.pushButton.setText(_translate("MainWindow", "Ok"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
