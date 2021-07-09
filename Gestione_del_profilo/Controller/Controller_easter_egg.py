from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_del_profilo.View.PyLemon_easter_egg import Easter_egg


class controller_easter_egg(QtWidgets.QWidget,Easter_egg):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)