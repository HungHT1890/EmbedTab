# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\ViewChromeForm\GUI\embed_tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FormView(object):
    def setupUi(self, FormView):
        FormView.setObjectName("FormView")
        FormView.resize(1600, 578)
        self.gridLayout = QtWidgets.QGridLayout(FormView)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(FormView)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1580, 558))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(FormView)
        QtCore.QMetaObject.connectSlotsByName(FormView)

    def retranslateUi(self, FormView):
        _translate = QtCore.QCoreApplication.translate
        FormView.setWindowTitle(_translate("FormView", "View Chrome"))