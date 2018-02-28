import sys
import sys
from widget import *
from PyQt4 import QtGui

class Barra(QtGui.QDialog):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.ui.verticalSlider.valueChanged.connect(self.verticalS)
        self.ui.horizontalSlider.valueChanged.connect(self.horizontalV)
        self.ui.verticalScrollBar.valueChanged.connect(self.verticalV)
        self.ui.horizontalScrollBar.valueChanged.connect(self.horizontalS)

    def verticalS(self,value):
        self.ui.saida.setText(str(value))
        self.ui.verticalScrollBar.setValue(value)

    def horizontalV(self,value):
        self.ui.saida.setText(str(value))
        self.ui.horizontalScrollBar.setValue(value)

    def verticalV(self,value):
        self.ui.saida.setText(str(value))
        self.ui.verticalSlider.setValue(value)

    def horizontalS(self,value):
        self.ui.saida.setText(str(value))
        self.ui.horizontalSlider.setValue(value)
app = QtGui.QApplication(sys.argv)
myapp = Barra()
myapp.show()
app.exec_()