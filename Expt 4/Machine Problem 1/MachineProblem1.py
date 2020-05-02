# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MachineProblem.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(243, 197)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(20, 20, 201, 131))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Label_Cel = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Label_Cel.setFont(font)
        self.Label_Cel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Cel.setObjectName("Label_Cel")
        self.verticalLayout_10.addWidget(self.Label_Cel)
        self.Label_Fah = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(13)
        self.Label_Fah.setFont(font)
        self.Label_Fah.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Label_Fah.setObjectName("Label_Fah")
        self.verticalLayout_10.addWidget(self.Label_Fah)
        self.horizontalLayout_4.addLayout(self.verticalLayout_10)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.LineEdit_Cel = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.LineEdit_Cel.setFont(font)
        self.LineEdit_Cel.setObjectName("LineEdit_Cel")
        self.verticalLayout_5.addWidget(self.LineEdit_Cel)
        self.LineEdit_Fah = QtWidgets.QLineEdit(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.LineEdit_Fah.setFont(font)
        self.LineEdit_Fah.setObjectName("LineEdit_Fah")
        self.verticalLayout_5.addWidget(self.LineEdit_Fah)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PushButton_FahToCel = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.PushButton_FahToCel.setObjectName("PushButton_FahToCel")
        self.PushButton_FahToCel.clicked.connect(self.fahToCel)
        self.horizontalLayout.addWidget(self.PushButton_FahToCel)
        self.PushButton_CelToFah = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.PushButton_CelToFah.setObjectName("PushButton_CelToFah")
        self.PushButton_CelToFah.clicked.connect(self.celToFah)
        self.horizontalLayout.addWidget(self.PushButton_CelToFah)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PushButton_Reset = QtWidgets.QPushButton(self.verticalLayoutWidget_3)
        self.PushButton_Reset.setObjectName("PushButton_Reset")
        self.PushButton_Reset.clicked.connect(self.reset)
        self.horizontalLayout_2.addWidget(self.PushButton_Reset)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 243, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Temp Converter"))
        self.Label_Cel.setText(_translate("MainWindow", "Celsius:"))
        self.Label_Fah.setText(_translate("MainWindow", "Fahrenheit:"))
        self.PushButton_FahToCel.setText(_translate("MainWindow", ">>>>"))
        self.PushButton_CelToFah.setText(_translate("MainWindow", "<<<<"))
        self.PushButton_Reset.setText(_translate("MainWindow", "Reset"))
        
        self.reset
        
    #Convert Fahrenheit to Celcius
    def fahToCel(self):
        cel = (float(self.LineEdit_Fah.text()) - 32) * 5/9
        fCel = round(cel, 2)
        self.LineEdit_Cel.setText(str(fCel))
    
    #Convert Celcius to Fahrenheit
    def celToFah(self):
        fah = (float(self.LineEdit_Cel.text()) * 9/5) + 32
        fFah = round(fah, 2)
        self.LineEdit_Fah.setText(str(fFah))
    
    #Reset Textboxes to default values
    def reset(self):
        self.LineEdit_Cel.setText(str(0.0))
        self.LineEdit_Fah.setText(str(32.0))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

