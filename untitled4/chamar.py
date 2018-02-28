import sys
from widget import *
from PyQt4 import QtGui


class Calcular(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.botao,QtCore.SIGNAL("clicked()"),self.calcular)

    def calcular(self):
        calculo = int(self.ui.preco.text())*int(self.ui.quantidade.text())-int(self.ui.preco.text())*int(self.ui.porcentagem.text())
        self.ui.resultador.setText("Total a pagar:"+str(calculo))

app = QtGui.QApplication(sys.argv)
myapp = Calcular()
myapp.show()
app.exec_()