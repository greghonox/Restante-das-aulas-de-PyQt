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
        Widget.resize(372, 165)
        self.linha_numero = QtGui.QLineEdit(Widget)
        self.linha_numero.setEnabled(False)
        self.linha_numero.setGeometry(QtCore.QRect(250, 30, 113, 25))
        self.linha_numero.setObjectName(_fromUtf8("linha_numero"))
        self.linha_numero_double = QtGui.QLineEdit(Widget)
        self.linha_numero_double.setEnabled(False)
        self.linha_numero_double.setGeometry(QtCore.QRect(250, 90, 113, 25))
        self.linha_numero_double.setObjectName(_fromUtf8("linha_numero_double"))
        self.layoutWidget = QtGui.QWidget(Widget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 170, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.numero = QtGui.QSpinBox(self.layoutWidget)
        self.numero.setObjectName(_fromUtf8("numero"))
        self.horizontalLayout.addWidget(self.numero)
        self.layoutWidget1 = QtGui.QWidget(Widget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 80, 217, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setMargin(11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_2.addWidget(self.label_2)
        self.numeroDouble = QtGui.QDoubleSpinBox(self.layoutWidget1)
        self.numeroDouble.setObjectName(_fromUtf8("numeroDouble"))
        self.horizontalLayout_2.addWidget(self.numeroDouble)
        self.botao = QtGui.QPushButton(Widget)
        self.botao.setGeometry(QtCore.QRect(280, 130, 79, 25))
        self.botao.setObjectName(_fromUtf8("botao"))
        self.saida = QtGui.QLabel(Widget)
        self.saida.setGeometry(QtCore.QRect(20, 140, 231, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.saida.setFont(font)
        self.saida.setObjectName(_fromUtf8("saida"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.label.setText(_translate("Widget", "Selecione o valor", None))
        self.label_2.setText(_translate("Widget", "Selecione outro valor", None))
        self.botao.setText(_translate("Widget", "Calcular", None))
        self.saida.setText(_translate("Widget", "Saida:", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

