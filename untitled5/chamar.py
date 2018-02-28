import sys
import sys
from widget import *
from PyQt4 import QtGui

class Radio(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.botao,QtCore.SIGNAL("clicked()"),self.calcular)

    def calcular(self):

        if(self.ui.multiplicacao.isChecked() == True):
            calculo = int(self.ui.caixa_1.text())*int(self.ui.caixa_2.text())
        elif(self.ui.soma.isChecked() == True ):
            calculo = int(self.ui.caixa_1.text())+int(self.ui.caixa_2.text())            
        elif(self.ui.subt.isChecked() == True ):
            calculo = int(self.ui.caixa_1.text())-int(self.ui.caixa_2.text())            
        elif(self.ui.divisao.isChecked() == True ):
            calculo = int(self.ui.caixa_1.text())/int(self.ui.caixa_2.text())            
        
        

        self.ui.resultado.setText("Resultado:"+str(calculo))

app = QtGui.QApplication(sys.argv)
myapp = Radio()
myapp.show()
app.exec_()