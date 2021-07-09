

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QMovie



'''-------------------Classe view Home ascoltatore---------------------'''

class home_ascoltatore(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 508)
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")



        '''---------Titolo finestra--------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 20, 381, 41))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")



        """------------Bottone mostra tutte-----------"""

        self.btn_mostraTutte = QtWidgets.QPushButton(Form)
        self.btn_mostraTutte.setGeometry(QtCore.QRect(490, 125, 80, 70))
        self.btn_mostraTutte.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                           "border-radius: 20px;\n"
                                           "color: 'white';}" +
                                           "*:hover{background: rgb(130, 130, 130);\n}")

        self.btn_mostraTutte.setText("")
        self.btn_mostraTutte.setObjectName("pushButton")
        self.btn_mostraTutte.setIcon(QIcon('Show_all_icon.png'))
        self.btn_mostraTutte.setIconSize(QtCore.QSize(60, 60))



        """-------------Bottone search------------"""

        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(70, 130, 70, 61))
        self.btn_search.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                       "border-radius: 20px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(130, 130, 130);\n}")
        self.btn_search.setText("")
        self.btn_search.setObjectName("pushButton_4")
        self.btn_search.setIcon(QIcon('Lente.png'))
        self.btn_search.setIconSize(QtCore.QSize(120, 120))



        """----------Barra Search----------"""

        self.txt_nome = QtWidgets.QLineEdit(Form)
        self.txt_nome.setGeometry(QtCore.QRect(155, 130, 320, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.txt_nome.sizePolicy().hasHeightForWidth())
        self.txt_nome.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txt_nome.setFont(font)
        self.txt_nome.setTabletTracking(False)
        self.txt_nome.setStyleSheet("background-color: rgb(207, 207, 207);\n"
                                    "color: rgb(55, 55, 55);\n"
                                    "border-radius: 20px;\n"
                                    "border-color: rgb(133, 133, 133);")
        self.txt_nome.setObjectName("lineEdit")



        '''-----------ListView Playlist----------'''

        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(250, 280, 231, 211))
        self.listView.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                      "background-color: rgb(51, 51, 51);"
                                      "border-radius: 5px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.listView.setObjectName("listView_2")



        '''-----------Linee separazione----------'''

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(0, 260, 651, 16))
        self.line.setMinimumSize(QtCore.QSize(2, 2))
        self.line.setStyleSheet("color: rgb(207, 207, 207);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line_9")
        self.line_1 = QtWidgets.QFrame(Form)
        self.line_1.setGeometry(QtCore.QRect(220, 270, 20, 231))
        self.line_1.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_1.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_1.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_1.setObjectName("line_10")



        '''------------Top 5------------'''

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(20, 280, 191, 211))
        self.table.setMinimumSize(QtCore.QSize(3, 0))
        self.table.setMouseTracking(False)
        self.table.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"   
                                 "background-color: rgb(51, 51, 51);"
                                 "border-radius: 5px;\n"
                                 "font: 10pt \"Arial\";"
                                 "color: 'white';}")
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setLineWidth(0)
        self.table.setMidLineWidth(0)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setAutoScroll(False)
        self.table.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
        self.table.setDragDropOverwriteMode(False)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setShowGrid(False)
        self.table.setGridStyle(QtCore.Qt.NoPen)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem();
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table.setHorizontalHeaderItem(2, item)
        self.table.horizontalHeader().setVisible(True)
        self.table.horizontalHeader().setHighlightSections(True)
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setHighlightSections(True)



        '''------------Bottone impostazioni------------'''

        self.btn_Impostazioni = QtWidgets.QPushButton(Form)
        self.btn_Impostazioni.setGeometry(QtCore.QRect(520, 330, 91, 21))
        self.btn_Impostazioni.setMouseTracking(True)
        self.btn_Impostazioni.setTabletTracking(True)
        self.btn_Impostazioni.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Impostazioni.setObjectName("pushButton_3")



        '''------------Bottone log out------------'''

        self.btn_Logout = QtWidgets.QPushButton(Form)
        self.btn_Logout.setGeometry(QtCore.QRect(520, 380, 91, 21))
        self.btn_Logout.setMouseTracking(True)
        self.btn_Logout.setTabletTracking(True)
        self.btn_Logout.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                        "border-radius: 10px;\n"
                                        "font: 10pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Logout.setObjectName("pushButton_4")



        '''-----------Bottone limone (Easter egg)---------'''

        self.btn_limone = QtWidgets.QPushButton(Form)
        self.btn_limone.setGeometry(QtCore.QRect(530, 430, 70, 65))
        font = QtGui.QFont()
        self.btn_limone.setFont(font)
        self.btn_limone.setStyleSheet("*{border: 0.5px solid rgb(40, 39, 39);"
                                       "border-radius: 25px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}")
        self.btn_limone.setText("")
        self.btn_limone.setObjectName("btn_limone")
        self.btn_limone.setIcon(QIcon('Limone.png'))
        self.btn_limone.setIconSize(QtCore.QSize(100, 100))



        '''------------Scritta "Playlist"-------------'''

        self.label_coming = QtWidgets.QLabel(Form)
        self.label_coming.setGeometry(QtCore.QRect(338, 305, 100, 30))
        self.label_coming.setStyleSheet("background-color: rgb(51, 51, 51);"
                                         "color: rgb(255, 252, 252);\n"
                                         "font: 15pt \".AppleSystemUIFont\";")
        self.label_coming.setObjectName("label_coming")



        '''-------------------Coming soon GIF--------------------'''

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(305, 330, 120, 120))
        self.centralwidget.setStyleSheet("background-color: rgb(51, 51, 51);"
                                        "color: rgb(255, 252, 252);\n"
                                        "font: 15pt \".AppleSystemUIFont\";")
        self.gif_coming = QtWidgets.QLabel(self.centralwidget)
        self.gif_coming.setGeometry(QtCore.QRect(10, -15, 300, 300))
        self.gif_coming.setMinimumSize(QtCore.QSize(150, 150))
        self.gif_coming.setMaximumSize(QtCore.QSize(150, 150))

        self.gif_coming.setObjectName("gif")
        self.movie = QMovie("comingsoon.gif")
        self.movie.setScaledSize(QSize().scaled(100, 100, Qt.KeepAspectRatio))
        self.gif_coming.setMovie(self.movie)
        self.movie.start()



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon ascoltatore"))
        self.btn_mostraTutte.setText(_translate("Form", ""))
        self.btn_Impostazioni.setText(_translate("Form", "Impostazioni"))
        self.btn_Logout.setText(_translate("Form", "Log out"))
        self.btn_search.setText(_translate("Form", ""))
        self.btn_limone.setText(_translate("Form", ""))
        self.label_coming.setText(_translate("Form", "Playlist"))

        self.txt_nome.setPlaceholderText(_translate("Form", " Search..."))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "TOP 5 "))
        font1 = QtGui.QFont().bold()
        font = QtGui.QFont("Arial", 10, font1)
        item.setFont(font)
        self.table.setColumnWidth(0, 191)

'''app = QApplication([])
window = QWidget()
form = home_ascoltatore()
form.setupUi(window)
window.show()
app.exec()'''