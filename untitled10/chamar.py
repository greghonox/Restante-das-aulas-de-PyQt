import sys
from PyQt4 import QtCore, QtGui
from main import *

class multi_janelas(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QtCore.QObject.connect(self.ui.ver_seguinte,QtCore.SIGNAL("clicked()"),self.ver_seguinte)
        QtCore.QObject.connect(self.ui.ver_anterior,QtCore.SIGNAL("clicked()"),self.ver_anterior)

    def ver_seguinte(self):
        self.ui.mdiArea.showFullScreen()
    def ver_anterior(self):
        self.ui.mdiArea.setViewMode(0)


app = QtGui.QApplication(sys.argv)
myapp = multi_janelas()
myapp.show()
app.exec_()