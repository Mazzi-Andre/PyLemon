

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QMovie



'''-------------------Classe view Home etichetta--------------------'''

class home_etichetta(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(910, 515)
        Form.setMinimumSize(QtCore.QSize(910, 515))
        Form.setMaximumSize(QtCore.QSize(910, 515))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''---------Titolo finestra--------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(255, 10, 430, 90))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")

        """----------Barra Search----------"""
        self.txt_nome = QtWidgets.QLineEdit(Form)
        self.txt_nome.setGeometry(QtCore.QRect(260, 130, 390, 61))
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



        """------------Bottone mostra tutte-----------"""

        self.btn_mostraTutte = QtWidgets.QPushButton(Form)
        self.btn_mostraTutte.setGeometry(QtCore.QRect(665, 130, 90, 61))
        self.btn_mostraTutte.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                           "border-radius: 20px;\n"
                                           "color: 'white';}" +
                                           "*:hover{background: rgb(130, 130, 130);\n}")

        self.btn_mostraTutte.setText("")
        self.btn_mostraTutte.setObjectName("pushButton")
        self.btn_mostraTutte.setIcon(QIcon('Data/photo/Show_all_icon.png'))
        self.btn_mostraTutte.setIconSize(QtCore.QSize(60, 60))



        """-------------Bottone search------------"""

        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(170, 130, 70, 61))
        self.btn_search.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                       "border-radius: 20px;\n"
                                       "color: 'white';}" +
                                       "*:hover{background: rgb(130, 130, 130);\n}")
        self.btn_search.setText("")
        self.btn_search.setObjectName("pushButton_4")
        self.btn_search.setIcon(QIcon('Data/photo/Lente.png'))
        self.btn_search.setIconSize(QtCore.QSize(120, 120))



        '''-----------Linee separazione--------'''

        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(0, 270, 911, 16))
        self.line_2.setMinimumSize(QtCore.QSize(2, 2))
        self.line_2.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(210, 280, 20, 231))
        self.line_3.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(470, 280, 20, 231))
        self.line_4.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")


        '''-----------Bottone pubblica----------'''

        self.btn_Pubblica = QtWidgets.QPushButton(Form)
        self.btn_Pubblica.setGeometry(QtCore.QRect(770, 350, 91, 21))
        self.btn_Pubblica.setMouseTracking(True)
        self.btn_Pubblica.setTabletTracking(True)
        self.btn_Pubblica.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);" 
                                        "border-radius: 10px;\n"
                                        "font: 7pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Pubblica.setObjectName("pushButton_2")


        '''------------Bottone impostazioni------------'''

        self.btn_Impostazioni = QtWidgets.QPushButton(Form)
        self.btn_Impostazioni.setGeometry(QtCore.QRect(770, 300, 91, 21))
        self.btn_Impostazioni.setMouseTracking(True)
        self.btn_Impostazioni.setTabletTracking(True)
        self.btn_Impostazioni.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                        "border-radius: 10px;\n"
                                        "font: 7pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Impostazioni.setObjectName("pushButton_3")


        '''------------Bottone log out------------'''

        self.btn_Logout = QtWidgets.QPushButton(Form)
        self.btn_Logout.setGeometry(QtCore.QRect(770, 400, 91, 21))
        self.btn_Logout.setMouseTracking(True)
        self.btn_Logout.setTabletTracking(True)
        self.btn_Logout.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                        "border-radius: 10px;\n"
                                        "font: 7pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Logout.setObjectName("pushButton_4")


        '''-----------ListView Playlist e miei artisti----------'''

        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(493, 290, 231, 211))
        self.listView.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"  
                                      "background-color: rgb(51, 51, 51);"
                                      "border-radius: 5px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.listView.setObjectName("listView")

        self.listView_2 = QtWidgets.QListView(Form)
        self.listView_2.setGeometry(QtCore.QRect(230, 290, 235, 211))
        self.listView_2.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                      "background-color: rgb(51, 51, 51);"
                                      "border-radius: 5px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.listView_2.setObjectName("listView_2")


        '''------------Top 5------------'''

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(20, 290, 191, 211))
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


        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 169, 30))
        self.label_2.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                   "background-color: rgb(51, 51, 51);"
                                   "border-radius: 5px;\n"
                                   "color: 'white';}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_3")


        '''-----------Bottone limone (Easter egg)---------'''
        self.btn_limone = QtWidgets.QPushButton(Form)
        self.btn_limone.setGeometry(QtCore.QRect(780, 435, 70, 77))
        font = QtGui.QFont()
        self.btn_limone.setFont(font)
        self.btn_limone.setStyleSheet("*{border: 0.5px solid rgb(40, 39, 39);"
                                      "border-radius: 25px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.btn_limone.setText("")
        self.btn_limone.setObjectName("btn_limone")
        self.btn_limone.setIcon(QIcon('Data/photo/Limone.png'))
        self.btn_limone.setIconSize(QtCore.QSize(120, 120))




        '''------------Scritta "Playlist"-------------'''

        self.label_coming_playlist = QtWidgets.QLabel(Form)
        self.label_coming_playlist.setGeometry(QtCore.QRect(585, 305, 100, 30))
        self.label_coming_playlist.setStyleSheet("background-color: rgb(51, 51, 51);"
                                        "color: rgb(255, 252, 252);\n"
                                        "font: 10pt \".AppleSystemUIFont\";")
        self.label_coming_playlist.setObjectName("label_coming")




        '''------------Scritta "Tuoi artisti"-------------'''
        self.label_coming_miei_artisti = QtWidgets.QLabel(Form)
        self.label_coming_miei_artisti.setGeometry(QtCore.QRect(305, 305, 100, 30))
        self.label_coming_miei_artisti.setStyleSheet("background-color: rgb(51, 51, 51);"
                                        "color: rgb(255, 252, 252);\n"
                                        "font: 10pt \".AppleSystemUIFont\";")
        self.label_coming_miei_artisti.setObjectName("label_coming")




        '''-------------------Coming soon GIF--------------------'''

        self.centralwidget_1 = QtWidgets.QWidget(Form)
        self.centralwidget_1.setObjectName("centralwidget")
        self.centralwidget_1.setGeometry(QtCore.QRect(285, 330, 120, 120))
        self.centralwidget_1.setStyleSheet("background-color: rgb(51, 51, 51);"
                                         "color: rgb(255, 252, 252);\n"
                                         "font: 15pt \".AppleSystemUIFont\";")
        self.gif_coming_1 = QtWidgets.QLabel(self.centralwidget_1)
        self.gif_coming_1.setGeometry(QtCore.QRect(10, -15, 300, 300))
        self.gif_coming_1.setMinimumSize(QtCore.QSize(150, 150))
        self.gif_coming_1.setMaximumSize(QtCore.QSize(150, 150))

        self.gif_coming_1.setObjectName("gif")
        self.movie_1 = QMovie("Data/gif/comingsoon.gif")
        self.movie_1.setScaledSize(QSize().scaled(100, 100, Qt.KeepAspectRatio))
        self.gif_coming_1.setMovie(self.movie_1)
        self.movie_1.start()


        self.centralwidget_2 = QtWidgets.QWidget(Form)
        self.centralwidget_2.setObjectName("centralwidget")
        self.centralwidget_2.setGeometry(QtCore.QRect(550, 330, 120, 120))
        self.centralwidget_2.setStyleSheet("background-color: rgb(51, 51, 51);"
                                         "color: rgb(255, 252, 252);\n"
                                         "font: 15pt \".AppleSystemUIFont\";")
        self.gif_coming_2 = QtWidgets.QLabel(self.centralwidget_2)
        self.gif_coming_2.setGeometry(QtCore.QRect(10, -15, 300, 300))
        self.gif_coming_2.setMinimumSize(QtCore.QSize(150, 150))
        self.gif_coming_2.setMaximumSize(QtCore.QSize(150, 150))

        self.gif_coming_2.setObjectName("gif")
        self.movie_2 = QMovie("Data/gif/comingsoon.gif")
        self.movie_2.setScaledSize(QSize().scaled(100, 100, Qt.KeepAspectRatio))
        self.gif_coming_2.setMovie(self.movie_2)
        self.movie_2.start()



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.txt_nome.setPlaceholderText(_translate("Form", "  Search..."))
        self.label.setText(_translate("Form", "PyLemon etichetta"))
        self.btn_mostraTutte.setText(_translate("Form", ""))
        self.btn_Pubblica.setText(_translate("Form", "Pubblica"))
        self.btn_Impostazioni.setText(_translate("Form", "Impostazioni"))
        self.btn_Logout.setText(_translate("Form", "Log out"))
        self.btn_search.setText(_translate("Form", ""))
        self.btn_limone.setText(_translate("Form", ""))
        self.label_coming_playlist.setText(_translate("Form", "Playlist"))
        self.label_coming_miei_artisti.setText(_translate("Form", "I tuoi artisti"))
        self.label_2.setText(_translate("Form", "  TOP 5"))

        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "TOP 5 "))
        font1 = QtGui.QFont().bold()
        font = QtGui.QFont("Arial", 10, font1)
        item.setFont(font)
        self.table.setColumnWidth(0, 191)