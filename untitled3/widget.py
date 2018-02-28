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
        Widget.resize(242, 257)
        self.botao = QtGui.QPushButton(Widget)
        self.botao.setGeometry(QtCore.QRect(100, 210, 83, 25))
        self.botao.setObjectName(_fromUtf8("botao"))
        self.label = QtGui.QLabel(Widget)
        self.label.setGeometry(QtCore.QRect(80, 40, 64, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Widget)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 64, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Widget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 64, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.primeiro = QtGui.QLineEdit(Widget)
        self.primeiro.setGeometry(QtCore.QRect(110, 90, 113, 25))
        self.primeiro.setObjectName(_fromUtf8("primeiro"))
        self.segundo = QtGui.QLineEdit(Widget)
        self.segundo.setGeometry(QtCore.QRect(110, 150, 113, 25))
        self.segundo.setObjectName(_fromUtf8("segundo"))

        self.retranslateUi(Widget)
        QtCore.QMetaObject.connectSlotsByName(Widget)

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(_translate("Widget", "Widget", None))
        self.botao.setText(_translate("Widget", "somar", None))
        self.label.setText(_translate("Widget", "saida", None))
        self.label_2.setText(_translate("Widget", "TextLabel", None))
        self.label_3.setText(_translate("Widget", "TextLabel", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Widget = QtGui.QWidget()
    ui = Ui_Widget()
    ui.setupUi(Widget)
    Widget.show()
    sys.exit(app.exec_())

