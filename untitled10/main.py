# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1050, 547)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.mdiArea = QtGui.QMdiArea(self.centralWidget)
        self.mdiArea.setGeometry(QtCore.QRect(10, 10, 1011, 311))
        self.mdiArea.setObjectName(_fromUtf8("mdiArea"))
        self.subwindow = QtGui.QWidget()
        self.subwindow.setObjectName(_fromUtf8("subwindow"))
        self.label_2 = QtGui.QLabel(self.subwindow)
        self.label_2.setGeometry(QtCore.QRect(180, 0, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lcdNumber = QtGui.QLCDNumber(self.subwindow)
        self.lcdNumber.setGeometry(QtCore.QRect(80, 50, 64, 23))
        self.lcdNumber.setObjectName(_fromUtf8("lcdNumber"))
        self.subwindow_2 = QtGui.QWidget()
        self.subwindow_2.setObjectName(_fromUtf8("subwindow_2"))
        self.label = QtGui.QLabel(self.subwindow_2)
        self.label.setGeometry(QtCore.QRect(170, 10, 111, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.calendarWidget = QtGui.QCalendarWidget(self.subwindow_2)
        self.calendarWidget.setGeometry(QtCore.QRect(100, 60, 288, 171))
        self.calendarWidget.setObjectName(_fromUtf8("calendarWidget"))
        self.layoutWidget = QtGui.QWidget(self.centralWidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 330, 121, 101))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setMargin(11)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.ver_seguinte = QtGui.QPushButton(self.layoutWidget)
        self.ver_seguinte.setObjectName(_fromUtf8("ver_seguinte"))
        self.verticalLayout_3.addWidget(self.ver_seguinte)
        self.cascata = QtGui.QPushButton(self.layoutWidget)
        self.cascata.setObjectName(_fromUtf8("cascata"))
        self.verticalLayout_3.addWidget(self.cascata)
        self.layoutWidget1 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(514, 330, 141, 101))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setMargin(11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.fechar_tudo = QtGui.QPushButton(self.layoutWidget1)
        self.fechar_tudo.setObjectName(_fromUtf8("fechar_tudo"))
        self.verticalLayout.addWidget(self.fechar_tudo)
        self.ver_janelas = QtGui.QPushButton(self.layoutWidget1)
        self.ver_janelas.setObjectName(_fromUtf8("ver_janelas"))
        self.verticalLayout.addWidget(self.ver_janelas)
        self.layoutWidget2 = QtGui.QWidget(self.centralWidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(280, 330, 131, 101))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_2.setMargin(11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ver_anterior = QtGui.QPushButton(self.layoutWidget2)
        self.ver_anterior.setObjectName(_fromUtf8("ver_anterior"))
        self.verticalLayout_2.addWidget(self.ver_anterior)
        self.mosaico = QtGui.QPushButton(self.layoutWidget2)
        self.mosaico.setObjectName(_fromUtf8("mosaico"))
        self.verticalLayout_2.addWidget(self.mosaico)
        MainWindow.setCentralWidget(self.centralWidget)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.subwindow.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.label_2.setText(_translate("MainWindow", "Primeira janela", None))
        self.subwindow_2.setWindowTitle(_translate("MainWindow", "Subwindow", None))
        self.label.setText(_translate("MainWindow", "Segunda Janela", None))
        self.ver_seguinte.setText(_translate("MainWindow", "ver seguinte", None))
        self.cascata.setText(_translate("MainWindow", "cascata", None))
        self.fechar_tudo.setText(_translate("MainWindow", "fechar tudo", None))
        self.ver_janelas.setText(_translate("MainWindow", "Ver janelas", None))
        self.ver_anterior.setText(_translate("MainWindow", "ver anterior", None))
        self.mosaico.setText(_translate("MainWindow", "mosaico", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

