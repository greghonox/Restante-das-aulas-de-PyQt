import sys
from widget import *
from PyQt4 import QtGui

  
class Chamar(QtGui.QDialog):
    def __init__(self,parent=None):        
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.botao,QtCore.SIGNAL("clicked()"),self.somar)

    def somar(self):
        soma = int(self.ui.primeiro.text()) + int(self.ui.segundo.text())
        self.ui.label.setText("Soma: "+str(soma))             


app = QtGui.QApplication(sys.argv)
myapp = Chamar()
myapp.show()
app.exec_()