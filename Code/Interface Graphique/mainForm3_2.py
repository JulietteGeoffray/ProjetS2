# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm3_2.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 435)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 491, 368))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_etape3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_etape3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_etape3.setObjectName("label_etape3")
        self.gridLayout_3.addWidget(self.label_etape3, 0, 0, 1, 1)
        self.label_titre3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre3.setObjectName("label_titre3")
        self.gridLayout_3.addWidget(self.label_titre3, 1, 0, 1, 1)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_backStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_backStrainId.setObjectName("label_backStrainId")
        self.horizontalLayout_10.addWidget(self.label_backStrainId)
        self.lineEdit_backStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_backStrainId.setText("")
        self.lineEdit_backStrainId.setObjectName("lineEdit_backStrainId")
        self.horizontalLayout_10.addWidget(self.lineEdit_backStrainId)
        self.gridLayout_3.addLayout(self.horizontalLayout_10, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_ref = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_ref.setObjectName("label_ref")
        self.horizontalLayout.addWidget(self.label_ref)
        self.radioButton_yesRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_yesRef.setObjectName("radioButton_yesRef")
        self.horizontalLayout.addWidget(self.radioButton_yesRef)
        self.radioButton_noRef = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_noRef.setObjectName("radioButton_noRef")
        self.horizontalLayout.addWidget(self.radioButton_noRef)
        self.gridLayout_3.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_20 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_20.setObjectName("label_20")
        self.horizontalLayout_16.addWidget(self.label_20)
        self.label_mappStrainId = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_mappStrainId.setObjectName("label_mappStrainId")
        self.horizontalLayout_16.addWidget(self.label_mappStrainId)
        self.lineEdit_mappStrainId = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_mappStrainId.setText("")
        self.lineEdit_mappStrainId.setObjectName("lineEdit_mappStrainId")
        self.horizontalLayout_16.addWidget(self.lineEdit_mappStrainId)
        self.gridLayout_3.addLayout(self.horizontalLayout_16, 4, 0, 1, 1)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_dbsnp = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_dbsnp.setObjectName("label_dbsnp")
        self.horizontalLayout_17.addWidget(self.label_dbsnp)
        self.lineEdit_dbsnp = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_dbsnp.setText("")
        self.lineEdit_dbsnp.setObjectName("lineEdit_dbsnp")
        self.horizontalLayout_17.addWidget(self.lineEdit_dbsnp)
        self.toolButton_dbsnp = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_dbsnp.setObjectName("toolButton_dbsnp")
        self.horizontalLayout_17.addWidget(self.toolButton_dbsnp)
        self.gridLayout_3.addLayout(self.horizontalLayout_17, 5, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(470, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 6, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_back3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_back3.setObjectName("pushButton_back3")
        self.horizontalLayout_2.addWidget(self.pushButton_back3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_next3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_next3.setObjectName("pushButton_next3")
        self.horizontalLayout_2.addWidget(self.pushButton_next3)
        self.gridLayout_3.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 25))
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
        self.pushButton_acceuil.setText(_translate("MainWindow", "Acceuil"))
        self.pushButton_newAnalyse.setText(_translate("MainWindow", "Nouvelle analyse"))
        self.pushButton_oldAnalise.setText(_translate("MainWindow", "Charger une analyse"))
        self.pushButton_resultat.setText(_translate("MainWindow", "Résultats"))
        self.pushButton_author.setText(_translate("MainWindow", "About - Author"))
        self.label_etape3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 3 sur 4</span></p></body></html>"))
        self.label_titre3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Design of the population for the cartographie</span></p></body></html>"))
        self.label_backStrainId.setText(_translate("MainWindow", "Background strain ID  :                       "))
        self.label_ref.setText(_translate("MainWindow", "Referenced  :                                                 "))
        self.radioButton_yesRef.setText(_translate("MainWindow", "yes"))
        self.radioButton_noRef.setText(_translate("MainWindow", "no"))
        self.label_20.setToolTip(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt; font-style:italic;\">It should be the same as RGSM appearing in the $Mapping_gVCF (determine with &quot;Read Group&quot; information during analysis)</span></p></body></html>"))
        self.label_20.setText(_translate("MainWindow", "?"))
        self.label_mappStrainId.setText(_translate("MainWindow", "Mapping strain ID :                          "))
        self.label_dbsnp.setText(_translate("MainWindow", "dbSNP (background vs mapping)  :"))
        self.toolButton_dbsnp.setText(_translate("MainWindow", "..."))
        self.pushButton_back3.setText(_translate("MainWindow", "Back"))
        self.pushButton_next3.setText(_translate("MainWindow", "Next"))
