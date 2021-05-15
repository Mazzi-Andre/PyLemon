import os
import pathlib
import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets


# ---------- We dont Touch --------------------
from Login.controller.controller_login import Login


class Ui_Discovery(object):

    """" clesse riguardante l'applicazione """

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(682, 443)
        Form.setStyleSheet("background-color: rgb(11, 11, 11);")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(140, 70, 441, 251))
        self.tableWidget.setStyleSheet("background-color: rgb(189, 193, 193);\n"
                                       "color: rgb(27, 28, 28);")
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(270, 340, 181, 31))
        self.btn_submit.setStyleSheet("color: rgb(250, 255, 255);\n"
                                      "background-color: rgb(73, 199, 41);\n"
                                      "border-style:outset;\n"
                                      "border-radius:10px;\n"
                                      "font: 14pt \"Arial\";")
        self.btn_submit.setObjectName("btn_submit")
        self.l_title = QtWidgets.QLabel(Form)
        self.l_title.setGeometry(QtCore.QRect(220, 20, 251, 21))
        self.l_title.setStyleSheet("\n"
                                   "color:White;\n"
                                   "font: 18pt \".SF NS Text\";")
        self.l_title.setObjectName("l_title")
        self.btn_back = QtWidgets.QPushButton(Form)
        self.btn_back.setGeometry(QtCore.QRect(270, 390, 181, 31))
        self.btn_back.setStyleSheet("color: rgb(250, 255, 255);\n"
                                    "background-color: rgb(73, 199, 41);\n"
                                    "border-style:outset;\n"
                                    "border-radius:10px;\n"
                                    "font: 14pt \"Arial\";")
        self.btn_back.setObjectName("btn_back")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.btn_submit.clicked.connect(self.load_data)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_submit.setText(_translate("Form", "Submit"))
        self.l_title.setText(_translate("Form", "Automated Host Discovery "))
        self.btn_back.setText(_translate("Form", "Back"))


# ----------------------------------------------
from Registrazione.controller.controller_registrazione import Newuser


class Discovery(QtWidgets.QWidget, Ui_Discovery):
    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setupUi(self)
        self.btn_submit.clicked.connect(self.btn_submit_handler)
        self.btn_back.clicked.connect(self.btn_back_handler)

    def pop_message(self, text=""):
        msg = QtWidgets.QMessageBox()
        msg.setText("{}".format(text))
        msg.exec_()

    def load_data(self):
        self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem(str("Sr No")))
        self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(str(" Ip Address")))
        self.tableWidget.setItem(0, 2, QtWidgets.QTableWidgetItem(str("Mac Address")))
        self.tableWidget.setItem(0, 3, QtWidgets.QTableWidgetItem(str("Vendor")))

    def btn_submit_handler(self):
        self.load_data()

    def btn_back_handler(self):
        self.switch_window.emit()


class Controller:

    def __init__(self):
        pass

    def show_login_page(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_newuser_page)
        self.login.switch_window1.connect(self.show_discovery)
        self.login.show()

    def show_newuser_page(self):

        self.newuser = Newuser()
        self.newuser.switch_window.connect(self.show_login_page)
        self.login.close()
        self.newuser.show()

    def show_discovery(self):
        self.discovery = Discovery()
        self.discovery.switch_window.connect(self.show_login_page)
        self.login.close()
        self.discovery.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login_page()
    sys.exit(app.exec_())


#\Data\mp3
if __name__ == "__main__":
    main()
