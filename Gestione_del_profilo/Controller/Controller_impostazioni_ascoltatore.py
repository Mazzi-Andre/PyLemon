from PyQt5 import QtCore
from PyQt5 import QtWidgets

from Gestione_del_profilo.View.Impostazioni_ascoltatore import impostazioni_ascoltatore


'''----------classe controller view impostazioni ascoltatore----------'''

class controller_impostazioni_ascoltatore(QtWidgets.QWidget,impostazioni_ascoltatore):
    switch_window = QtCore.pyqtSignal()
    switch_window_1 = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_EliminaAccount.clicked.connect(self.btn_elimina_profilo_handler)
        self.btn_EditProfilo.clicked.connect(self.btn_edit_profilo_handler)



    """----------POP UP FINESTRA---------"""

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()


    """-----------SWITCH FINESTRE------------"""

    def btn_elimina_profilo_handler(self):
        self.switch_window.emit()

    def btn_edit_profilo_handler(self):
        self.switch_window_1.emit()
