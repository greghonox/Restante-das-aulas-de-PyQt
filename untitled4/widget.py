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
        Widget.resize(384, 216)
        self.botao = QtGui.QPushButton(Widget)
        self.botao.setGeometry(QtCore.QRect(280, 130, 83, 25))
        self.botao.setObjectName(_fromUtf8("botao"))
        self.quantidade = QtGui.QLineEdit(Widget)
        self.quantidade.setGeometry(QtCore.QRect(250, 10, 113, 25))
        self.quantidade.setObjectName(_fromUtf8("quantidade"))
        self.preco = QtGui.QLineEdit(Widget)
        self.preco.setGeometry(QtCore.QRect(250, 50, 113, 25))
        self.preco.setObjectName(_fromUtf8("preco"))
        self.porcentagem = QtGui.QLineEdit(Widget)
        self.porcentagem.setGeometry(QtCore.QRect(250, 90, 113, 25))
        self.porcentagem.setObjectName(_fromUtf8("porcentagem"))
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 101, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(10, 90, 91, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.resultador = QtGui.QLabel(Widget)
        self.resultador.setGeometry(QtCore.QRect(10, 170, 481, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.resultador.setFont(font)
        self.resultador.setText(_fromUtf8(""))
        self.resultador.setObjectName(_fromUtf8("resultador"))
        self.label.setBuddy(self.quantidade)
        self.label_2.setBuddy(self.preco)
        self.label_3.setBuddy(self.porcentagem)

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)
        Widget.setTabOrder(self.preco, self.quantidade)
        Widget.setTabOrder(self.quantidade, self.botao)
        Widget.setTabOrder(self.botao, self.porcentagem)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.botao.setText(_translate("Widget", "Calcular", None))
        self.label.setText(_translate("Widget", "Numero de itens", None))
        self.label_2.setText(_translate("Widget", "Preço dos itens", None))
        self.label_3.setText(_translate("Widget", "Desconto %", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

