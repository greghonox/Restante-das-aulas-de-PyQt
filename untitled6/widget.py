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
        Widget.resize(262, 253)
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(40, 10, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Latin Modern Roman"))
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(100, 150, 81, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.splitter = QtGui.QSplitter(Widget)
        self.splitter.setGeometry(QtCore.QRect(50, 50, 211, 92))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.processador = QtGui.QCheckBox(self.splitter)
        self.processador.setObjectName(_fromUtf8("processador"))
        self.memoria = QtGui.QCheckBox(self.splitter)
        self.memoria.setObjectName(_fromUtf8("memoria"))
        self.hd = QtGui.QCheckBox(self.splitter)
        self.hd.setObjectName(_fromUtf8("hd"))
        self.monitor = QtGui.QCheckBox(self.splitter)
        self.monitor.setObjectName(_fromUtf8("monitor"))
        self.splitter_2 = QtGui.QSplitter(Widget)
        self.splitter_2.setGeometry(QtCore.QRect(60, 170, 142, 67))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName(_fromUtf8("splitter_2"))
        self.caixa = QtGui.QLineEdit(self.splitter_2)
        self.caixa.setObjectName(_fromUtf8("caixa"))
        self.botao = QtGui.QPushButton(self.splitter_2)
        self.botao.setObjectName(_fromUtf8("botao"))
        self.resultado = QtGui.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("DejaVu Sans Mono"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.resultado.setFont(font)
        self.resultado.setText(_fromUtf8(""))
        self.resultado.setObjectName(_fromUtf8("resultado"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.label.setText(_translate("Widget", "MENU COMPUTADOR", None))
        self.label_2.setText(_translate("Widget", "Adicionais", None))
        self.processador.setText(_translate("Widget", "PROCESSADOR I3 R$ 800", None))
        self.memoria.setText(_translate("Widget", "MEMÓRIA 4GB R$ 200", None))
        self.hd.setText(_translate("Widget", "HD SSD 240 R$ 500", None))
        self.monitor.setText(_translate("Widget", "MONITOR LED 19\" R% 800", None))
        self.botao.setText(_translate("Widget", "CALCULAR", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

