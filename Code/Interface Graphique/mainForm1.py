# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainForm1.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(657, 416)
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
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        font = QtGui.QFont()
        font.setFamily("Latin Modern Mono")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.label_3.setAcceptDrops(False)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout_2.addWidget(self.pushButton_4, 1, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 2, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout_2.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout_2.addWidget(self.pushButton_5, 5, 0, 1, 1)
        self.gridLayout.addWidget(self.groupBox_2, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 377, 349))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_titre = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_titre.setMaximumSize(QtCore.QSize(16777215, 30))
        self.label_titre.setObjectName("label_titre")
        self.gridLayout_3.addWidget(self.label_titre, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_GenRef = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_GenRef.setObjectName("label_GenRef")
        self.horizontalLayout_4.addWidget(self.label_GenRef)
        self.lineEdit_GenRef = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_GenRef.setObjectName("lineEdit_GenRef")
        self.horizontalLayout_4.addWidget(self.lineEdit_GenRef)
        self.toolButton_GenRef = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_GenRef.setObjectName("toolButton_GenRef")
        self.horizontalLayout_4.addWidget(self.toolButton_GenRef)
        self.gridLayout_3.addLayout(self.horizontalLayout_4, 2, 0, 1, 3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_Read1 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Read1.setObjectName("label_Read1")
        self.horizontalLayout.addWidget(self.label_Read1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
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
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_Read2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_Read2.setObjectName("label_Read2")
        self.horizontalLayout_3.addWidget(self.label_Read2)
        self.lineEdit_Read2 = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.lineEdit_Read2.setObjectName("lineEdit_Read2")
        self.horizontalLayout_3.addWidget(self.lineEdit_Read2)
        self.toolButton_Read2 = QtWidgets.QToolButton(self.scrollAreaWidgetContents)
        self.toolButton_Read2.setObjectName("toolButton_Read2")
        self.horizontalLayout_3.addWidget(self.toolButton_Read2)
        self.gridLayout_3.addLayout(self.horizontalLayout_3, 4, 0, 1, 3)
        self.pushButton_plus = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_plus.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.gridLayout_3.addWidget(self.pushButton_plus, 5, 1, 1, 1)
        self.pushButton_moins = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_moins.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton_moins.setObjectName("pushButton_moins")
        self.gridLayout_3.addWidget(self.pushButton_moins, 5, 2, 1, 1)
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
        self.label_etape1.setObjectName("label_etape1")
        self.gridLayout_3.addWidget(self.label_etape1, 0, 0, 1, 3)
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
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">Andalusian Mapping</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "Acceuil"))
        self.pushButton.setText(_translate("MainWindow", "Nouvelle analyse"))
        self.pushButton_2.setText(_translate("MainWindow", "Charger une analyse"))
        self.pushButton_3.setText(_translate("MainWindow", "Résultats"))
        self.pushButton_5.setText(_translate("MainWindow", "About - Author"))
        self.label_titre.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\"># Your inputs :</span></p></body></html>"))
        self.label_GenRef.setText(_translate("MainWindow", "Génome de référence :    "))
        self.toolButton_GenRef.setText(_translate("MainWindow", "..."))
        self.label_Read1.setText(_translate("MainWindow", "[2] Séquences des reads :"))
        self.toolButton_Read1.setText(_translate("MainWindow", "..."))
        self.label_Read2.setText(_translate("MainWindow", "[1] Séquences des reads :"))
        self.toolButton_Read2.setText(_translate("MainWindow", "..."))
        self.pushButton_plus.setText(_translate("MainWindow", "-"))
        self.pushButton_moins.setText(_translate("MainWindow", "+"))
        self.pushButton_next1.setText(_translate("MainWindow", "Next"))
        self.label_etape1.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; font-style:italic;\">Formulaire : étape 1 sur 3</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
