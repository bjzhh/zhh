# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_w.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuOffice_tools = QtWidgets.QMenu(self.menubar)
        self.menuOffice_tools.setObjectName("menuOffice_tools")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionIFS = QtWidgets.QAction(MainWindow)
        self.actionIFS.setObjectName("actionIFS")
        self.actionCRM = QtWidgets.QAction(MainWindow)
        self.actionCRM.setObjectName("actionCRM")
        self.actionPAS = QtWidgets.QAction(MainWindow)
        self.actionPAS.setObjectName("actionPAS")
        self.actionESS = QtWidgets.QAction(MainWindow)
        self.actionESS.setObjectName("actionESS")
        self.actionOMS = QtWidgets.QAction(MainWindow)
        self.actionOMS.setObjectName("actionOMS")
        self.actionIMC = QtWidgets.QAction(MainWindow)
        self.actionIMC.setObjectName("actionIMC")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionExcel = QtWidgets.QAction(MainWindow)
        self.actionExcel.setObjectName("actionExcel")
        self.actionword = QtWidgets.QAction(MainWindow)
        self.actionword.setObjectName("actionword")
        self.menu.addAction(self.actionSave)
        self.menu.addAction(self.actionQuit)
        self.menu_2.addAction(self.actionIFS)
        self.menu_2.addAction(self.actionCRM)
        self.menu_2.addAction(self.actionPAS)
        self.menu_2.addAction(self.actionESS)
        self.menu_2.addAction(self.actionOMS)
        self.menu_2.addAction(self.actionIMC)
        self.menuOffice_tools.addAction(self.actionExcel)
        self.menuOffice_tools.addAction(self.actionword)
        self.menu_3.addAction(self.actionAbout)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuOffice_tools.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "快速入口"))
        self.menuOffice_tools.setTitle(_translate("MainWindow", "工具集"))
        self.menu_3.setTitle(_translate("MainWindow", "帮助"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionIFS.setText(_translate("MainWindow", "IFS"))
        self.actionCRM.setText(_translate("MainWindow", "CRM"))
        self.actionPAS.setText(_translate("MainWindow", "PAS"))
        self.actionESS.setText(_translate("MainWindow", "ESS"))
        self.actionOMS.setText(_translate("MainWindow", "OMS"))
        self.actionIMC.setText(_translate("MainWindow", "IMC"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionExcel.setText(_translate("MainWindow", "Excel拆分"))
        self.actionword.setText(_translate("MainWindow", "word"))
