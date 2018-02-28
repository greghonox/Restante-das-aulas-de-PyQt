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
        Widget.resize(263, 297)
        Widget.setStyleSheet(_fromUtf8("QWidget{\n"
"    background-color: 212, 254, 250;\n"
"}"))
        self.botao = QtGui.QPushButton(Widget)
        self.botao.setGeometry(QtCore.QRect(170, 110, 83, 25))
        self.botao.setObjectName(_fromUtf8("botao"))
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(170, 20, 64, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 64, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.resultado = QtGui.QLabel(Widget)
        self.resultado.setGeometry(QtCore.QRect(10, 250, 241, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Serif"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setText(_fromUtf8(""))
        self.resultado.setObjectName(_fromUtf8("resultado"))
        self.widget = QtGui.QWidget(Widget)
        self.widget.setGeometry(QtCore.QRect(0, 110, 151, 131))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.formLayout = QtGui.QFormLayout(self.widget)
        self.formLayout.setMargin(11)
        self.formLayout.setSpacing(6)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.soma = QtGui.QRadioButton(self.widget)
        self.soma.setObjectName(_fromUtf8("soma"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.soma)
        self.subt = QtGui.QRadioButton(self.widget)
        self.subt.setObjectName(_fromUtf8("subt"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.subt)
        self.divisao = QtGui.QRadioButton(self.widget)
        self.divisao.setObjectName(_fromUtf8("divisao"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.divisao)
        self.multiplicacao = QtGui.QRadioButton(self.widget)
        self.multiplicacao.setObjectName(_fromUtf8("multiplicacao"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.multiplicacao)
        self.splitter = QtGui.QSplitter(Widget)
        self.splitter.setGeometry(QtCore.QRect(10, 20, 142, 50))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.caixa_1 = QtGui.QLineEdit(self.splitter)
        self.caixa_1.setText(_fromUtf8(""))
        self.caixa_1.setObjectName(_fromUtf8("caixa_1"))
        self.caixa_2 = QtGui.QLineEdit(self.splitter)
        self.caixa_2.setObjectName(_fromUtf8("caixa_2"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.botao.setText(_translate("Widget", "calcular", None))
        self.label.setText(_translate("Widget", "Primeiro", None))
        self.label_2.setText(_translate("Widget", "Segundo", None))
        self.soma.setText(_translate("Widget", "soma", None))
        self.subt.setText(_translate("Widget", "subtração", None))
        self.divisao.setText(_translate("Widget", "divisão", None))
        self.multiplicacao.setText(_translate("Widget", "mutiplicação", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

