import sys
import sys
from widget import *
from PyQt4 import QtGui

class Chamar(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)        
        QtCore.QObject.connect(self.ui.numero,QtCore.SIGNAL("editingFinished()"),self.somaNumero)
        QtCore.QObject.connect(self.ui.numeroDouble,QtCore.SIGNAL("editingFinished()"),self.somaNumeroDouble)
        QtCore.QObject.connect(self.ui.botao,QtCore.SIGNAL("clicked()"),self.Calcular)

    def somaNumero(self):
        self.ui.linha_numero.setText(str(self.ui.numero.value()))
    def somaNumeroDouble(self):
        self.ui.linha_numero_double.setText(str(self.ui.numeroDouble.value()))
    def Calcular(self):
        self.ui.saida.setText("Saída:"+str(int(self.ui.numero.value())+ int(self.ui.numeroDouble.value()) ))

app = QtGui.QApplication(sys.argv)
myapp = Chamar()
myapp.show()
app.exec_()
