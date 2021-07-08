# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
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
        Dialog.setWindowModality(QtCore.Qt.NonModal)
        Dialog.resize(650, 190)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(650, 190))
        Dialog.setMaximumSize(QtCore.QSize(650, 190))
        Dialog.setFocusPolicy(QtCore.Qt.ClickFocus)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 5, 191, 19))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 150, 100, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(67, 67, 67))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.pushButton.setPalette(palette)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(120, 150, 100, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(10, 70, 630, 30))
        self.textEdit.setAcceptRichText(False)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(10, 110, 630, 30))
        self.textEdit_2.setAcceptRichText(False)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(10, 30, 630, 30))
        self.textEdit_3.setDocumentTitle("")
        self.textEdit_3.setAcceptRichText(False)
        self.textEdit_3.setObjectName("textEdit_3")
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setWindowFlags(Dialog.windowFlags() | QtCore.Qt.CustomizeWindowHint)
        Dialog.setWindowFlags(Dialog.windowFlags() & ~QtCore.Qt.WindowCloseButtonHint)
        self.Dialogs = Dialog
        self.pushButton.clicked.connect(self.Connect)
        self.pushButton_2.clicked.connect(Dialog.close)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Редактирование аккаунта"))
        self.pushButton.setText(_translate("Dialog", "Сохранить"))
        self.pushButton_2.setText(_translate("Dialog", "Отмена"))
        self.textEdit.setPlaceholderText(_translate("Dialog", "Api ключ"))
        self.textEdit_2.setPlaceholderText(_translate("Dialog", "Секретный ключ"))
        self.textEdit_3.setPlaceholderText(_translate("Dialog", "Название"))

    def Connect(self):
        private = self.textEdit_2.toPlainText()
        api = self.textEdit.toPlainText()
        name = self.textEdit_3.toPlainText()
        if (api != "" and private != "" and name != ""):
            self.api = api
            self.private = private
            self.name = name
            self.Dialogs.accept()

    def GetApi(self):
        return self.api, self.private, self.name