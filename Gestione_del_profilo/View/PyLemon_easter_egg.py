
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QMovie


'''------------------Classe view easter egg--------------'''

class Easter_egg(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 370)
        Form.setMinimumSize(QtCore.QSize(400, 370))
        Form.setMaximumSize(QtCore.QSize(400, 370))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''--------------Titolo finestra--------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(140, 30, 141, 51))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''---------------Lista nomi LemonCreatori--------------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(130, 200, 141, 21))
        self.label_2.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_2.setObjectName("label_3")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 230, 101, 21))
        self.label_3.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_3.setObjectName("label_4")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(150, 250, 121, 21))
        self.label_4.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_4.setObjectName("label_5")

        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(140, 270, 121, 21))
        self.label_5.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_5.setObjectName("label_6")

        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(140, 290, 111, 20))
        self.label_6.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_6.setObjectName("label_7")


        '''---------------LemonVersion----------------'''

        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(138, 330, 150, 16))
        self.label_7.setStyleSheet("color: rgb(207, 211, 211);")
        self.label_7.setObjectName("label_8")


        '''--------------GIF limone--------------'''

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.gif_label = QtWidgets.QLabel(self.centralwidget)
        self.gif_label.setGeometry(QtCore.QRect(80, 0, 140, 250))
        self.gif_label.setMinimumSize(QtCore.QSize(300, 200))
        self.gif_label.setMaximumSize(QtCore.QSize(300, 200))

        self.gif_label.setObjectName("gif")
        self.movie = QMovie("Limone-gif-unscreen.gif")
        self.movie.setScaledSize(QSize().scaled(400, 250, Qt.KeepAspectRatio))
        self.gif_label.setMovie(self.movie)
        self.movie.start()



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", ""))
        self.label_2.setText(_translate("Form", "       LemonCreatori:"))
        self.label_3.setText(_translate("Form", "    André Mazzi"))
        self.label_4.setText(_translate("Form", "   Andrea Tassi"))
        self.label_5.setText(_translate("Form", "    Manuel Mariotti"))
        self.label_6.setText(_translate("Form", "    Stefano Martelli"))
        self.label_7.setText(_translate("Form", "  LemonVersion: 1.0"))

