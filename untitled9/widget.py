# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'widget.ui'
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

class Ui_Widget(object):
    def setupUi(self, Widget):
        Widget.setObjectName(_fromUtf8("Widget"))
        Widget.resize(294, 300)
        self.botao = QtGui.QPushButton(Widget)
        self.botao.setGeometry(QtCore.QRect(190, 50, 83, 25))
        self.botao.setObjectName(_fromUtf8("botao"))
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, 20, 93, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.caixa = QtGui.QLineEdit(Widget)
        self.caixa.setGeometry(QtCore.QRect(130, 20, 142, 25))
        self.caixa.setObjectName(_fromUtf8("caixa"))
        self.listWidget = QtGui.QListWidget(Widget)
        self.listWidget.setGeometry(QtCore.QRect(20, 90, 256, 192))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton = QtGui.QPushButton(Widget)
        self.pushButton.setGeometry(QtCore.QRect(100, 50, 79, 25))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.editar = QtGui.QPushButton(Widget)
        self.editar.setGeometry(QtCore.QRect(0, 50, 79, 25))
        self.editar.setObjectName(_fromUtf8("editar"))

        self.retranslateUi(Widget)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.listWidget.clear)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.caixa, self.botao)
        Widget.setTabOrder(self.botao, self.pushButton)
        Widget.setTabOrder(self.pushButton, self.editar)
        Widget.setTabOrder(self.editar, self.listWidget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.botao.setText(_translate("Widget", "Inserir", None))
        self.label.setText(_translate("Widget", "Inserir na lista", None))
        self.pushButton.setText(_translate("Widget", "Limpar", None))
        self.editar.setText(_translate("Widget", "Editar", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

