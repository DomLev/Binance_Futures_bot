# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'delete.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class Ui_Dialog(QDialog):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(192, 105)
        Dialog.setMinimumSize(QtCore.QSize(192, 105))
        Dialog.setMaximumSize(QtCore.QSize(192, 105))
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 19))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 60, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 60, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(Dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        Dialog.setWindowFlags(Dialog.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.pushButton.clicked.connect(Dialog.accept)
        self.pushButton_2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Удалить аккаунт?"))
        self.pushButton.setText(_translate("Dialog", "Удалить"))
        self.pushButton_2.setText(_translate("Dialog", "Отмена"))
