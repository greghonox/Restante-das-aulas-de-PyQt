import sys
from widget import *
from PyQt4 import QtGui

class lista(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.botao, QtCore.SIGNAL("clicked()"),self.adicionar)
        QtCore.QObject.connect(self.ui.editar, QtCore.SIGNAL("clicked()"),self.editar)

    def adicionar(self):
        self.ui.listWidget.addItem(self.ui.caixa.text())
        self.ui.caixa.setText("")
        self.ui.caixa.setFocus()

    def editar(self):
        linha = self.ui.listWidget.currentRow()
        proxima, ok = QtGui.QInputDialog.getText(self,"Editar","Digite o valor correto")        
        if ok and (len(proxima) != 0):
            self.ui.listWidget.takeItem(self.ui.listWidget.currentRow())
            self.ui.listWidget.insertItem(linha,QtGui.QListWidgetItem(str(proxima)))

app = QtGui.QApplication(sys.argv)
myapp = lista()
myapp.show()
app.exec_()