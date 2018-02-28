import sys
import sys
from widget import *
from PyQt4 import QtGui

class menu_computador(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.botao,QtCore.SIGNAL("clicked()"),self.calcular)

    def calcular(self):
        valor = 0
        if(self.ui.processador.isChecked() == True):
            valor += 800
        if(self.ui.memoria.isChecked() == True):
            valor += 200
        if(self.ui.hd.isChecked() == True):
            valor += 500
        if(self.ui.monitor.isChecked()) :
            valor += 800
        if(self.ui.caixa.text() != 0):
            valor += int(self.ui.caixa.text())
        else:
            valor += 0
        self.ui.resultado.setText(str(valor))

app = QtGui.QApplication(sys.argv)
myapp = menu_computador()
myapp.show()
app.exec_()