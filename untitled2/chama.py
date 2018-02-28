import sys
from widget import *
from PyQt4 import QtGui

class soma(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.mostrar)

    def mostrar(self):
        self.ui.label.setText("Ola "+ self.ui.lineEdit.text()+" Tudo bem?")

app = QtGui.QApplication(sys.argv)
myapp = soma()
myapp.show()
app.exec_()