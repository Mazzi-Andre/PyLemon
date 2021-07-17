

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon, QMovie

'''-------------------Classe view Home artista--------------------'''


class home_artista(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(911, 515)
        Form.setMinimumSize(QtCore.QSize(911, 515))
        Form.setMaximumSize(QtCore.QSize(911, 515))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")

        '''-------------Titolo finestra------------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(280, 30, 381, 56))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 30pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")

        """-----------Bottone mostra tutte----------"""
        self.btn_mostraTutte = QtWidgets.QPushButton(Form)
        self.btn_mostraTutte.setGeometry(QtCore.QRect(665, 130, 90, 61))
        self.btn_mostraTutte.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                           "border-radius: 20px;\n"
                                           "color: 'white';}" +
                                           "*:hover{background: rgb(130, 130, 130);\n}")

        self.btn_mostraTutte.setText("")
        self.btn_mostraTutte.setObjectName("pushButton")
        self.btn_mostraTutte.setIcon(QIcon('Show_all_icon.png'))
        self.btn_mostraTutte.setIconSize(QtCore.QSize(60, 60))

        """-----------Bottone search---------"""
        self.btn_search = QtWidgets.QPushButton(Form)
        self.btn_search.setGeometry(QtCore.QRect(170, 130, 70, 61))
        self.btn_search.setStyleSheet("*{border: 1px solid rgb(40, 39, 39);"
                                      "border-radius: 20px;\n"
                                      "color: 'white';}" +
                                      "*:hover{background: rgb(130, 130, 130);\n}")
        self.btn_search.setText("")
        self.btn_search.setObjectName("pushButton_4")
        self.btn_search.setIcon(QIcon('Lente.png'))
        self.btn_search.setIconSize(QtCore.QSize(120, 120))

        """-----------Linea Search--------"""
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


        '''-----------Linee di separazione----------'''

        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(990, 340, 20, 271))
        self.line.setStyleSheet("color: rgb(207, 207, 207);")
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.line_2 = QtWidgets.QFrame(Form)
        self.line_2.setGeometry(QtCore.QRect(350, 610, 911, 16))
        self.line_2.setMinimumSize(QtCore.QSize(2, 2))
        self.line_2.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")

        self.line_4 = QtWidgets.QFrame(Form)
        self.line_4.setGeometry(QtCore.QRect(820, 620, 20, 231))
        self.line_4.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")

        self.line_3 = QtWidgets.QFrame(Form)
        self.line_3.setGeometry(QtCore.QRect(560, 620, 20, 231))
        self.line_3.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")

        self.line_5 = QtWidgets.QFrame(Form)
        self.line_5.setGeometry(QtCore.QRect(990, 340, 20, 271))
        self.line_5.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")

        self.line_6 = QtWidgets.QFrame(Form)
        self.line_6.setGeometry(QtCore.QRect(350, 610, 911, 16))
        self.line_6.setMinimumSize(QtCore.QSize(2, 2))
        self.line_6.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")

        self.line_7 = QtWidgets.QFrame(Form)
        self.line_7.setGeometry(QtCore.QRect(820, 620, 20, 231))
        self.line_7.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_7.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")

        self.line_8 = QtWidgets.QFrame(Form)
        self.line_8.setGeometry(QtCore.QRect(560, 620, 20, 231))
        self.line_8.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_8.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")

        self.line_9 = QtWidgets.QFrame(Form)
        self.line_9.setGeometry(QtCore.QRect(0, 270, 911, 16))
        self.line_9.setMinimumSize(QtCore.QSize(2, 2))
        self.line_9.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")

        self.line_10 = QtWidgets.QFrame(Form)
        self.line_10.setGeometry(QtCore.QRect(220, 280, 20, 231))
        self.line_10.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_10.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")

        self.line_11 = QtWidgets.QFrame(Form)
        self.line_11.setGeometry(QtCore.QRect(490, 280, 20, 231))
        self.line_11.setStyleSheet("color: rgb(207, 207, 207);")
        self.line_11.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")


        '''-----------Top 5-----------'''

        self.table_top = QtWidgets.QTableWidget(Form)
        self.table_top.setGeometry(QtCore.QRect(20, 290, 191, 211))
        self.table_top.setMinimumSize(QtCore.QSize(3, 0))
        self.table_top.setMouseTracking(False)
        self.table_top.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                     "background-color: rgb(51, 51, 51);"
                                     "border-radius: 5px;\n"
                                     "font: 10pt \"Arial\";"
                                     "color: 'white';}")
        self.table_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_top.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_top.setLineWidth(0)
        self.table_top.setMidLineWidth(0)
        self.table_top.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_top.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_top.setAutoScroll(False)
        self.table_top.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
        self.table_top.setDragDropOverwriteMode(False)
        self.table_top.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_top.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_top.setShowGrid(False)
        self.table_top.setGridStyle(QtCore.Qt.NoPen)
        self.table_top.setObjectName("table")
        self.table_top.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem();
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table_top.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table_top.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table_top.setHorizontalHeaderItem(2, item)
        self.table_top.horizontalHeader().setVisible(True)
        self.table_top.horizontalHeader().setHighlightSections(True)
        self.table_top.verticalHeader().setVisible(False)
        self.table_top.verticalHeader().setHighlightSections(True)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 290, 169, 30))
        self.label_2.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                   "background-color: rgb(51, 51, 51);"
                                   "border-radius: 5px;\n"
                                   "color: 'white';}")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")


        '''-----------Lista tuoi brani----------'''

        self.table_brani = QtWidgets.QTableWidget(Form)
        self.table_brani.setGeometry(QtCore.QRect(250, 290, 231, 211))
        self.table_brani.setMinimumSize(QtCore.QSize(3, 0))
        self.table_brani.setMouseTracking(False)
        self.table_brani.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                       "background-color: rgb(51, 51, 51);"
                                       "border-radius: 5px;\n"
                                       "font: 10pt \"Arial\";"
                                       "color: 'white';}")
        self.table_brani.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table_brani.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table_brani.setLineWidth(0)
        self.table_brani.setMidLineWidth(0)
        self.table_brani.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table_brani.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table_brani.setAutoScroll(False)
        self.table_brani.setEditTriggers(
                QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.SelectedClicked)
        self.table_brani.setDragDropOverwriteMode(False)
        self.table_brani.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_brani.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table_brani.setShowGrid(False)
        self.table_brani.setGridStyle(QtCore.Qt.NoPen)
        self.table_brani.setObjectName("table")
        self.table_brani.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem();
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)
        self.table_brani.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table_brani.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        item.setFont(font)

        self.table_brani.setHorizontalHeaderItem(2, item)
        self.table_brani.horizontalHeader().setVisible(True)
        self.table_brani.horizontalHeader().setHighlightSections(True)
        self.table_brani.verticalHeader().setVisible(False)
        self.table_brani.verticalHeader().setHighlightSections(True)

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(250, 290, 231, 30))
        self.label_3.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                   "background-color: rgb(51, 51, 51);"
                                   "border-radius: 5px;\n"
                                   "color: 'white';}")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")



        '''-----------ListView Playlist----------'''

        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(520, 290, 231, 211))
        self.listView.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                      "background-color: rgb(51, 51, 51);"
                                      "border-radius: 5px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.listView.setObjectName("listView_3")


        '''------------Bottone impostazioni-----------'''

        self.btn_Impostazioni = QtWidgets.QPushButton(Form)
        self.btn_Impostazioni.setGeometry(QtCore.QRect(780, 300, 91, 21))
        self.btn_Impostazioni.setMouseTracking(True)
        self.btn_Impostazioni.setTabletTracking(True)
        self.btn_Impostazioni.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                            "border-radius: 10px;\n"
                                            "font: 7pt \"Arial\";"
                                            "color: 'white';}" +
                                            "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Impostazioni.setObjectName("pushButton_3")


        '''-----------Bottone log out-----------'''

        self.btn_Logout = QtWidgets.QPushButton(Form)
        self.btn_Logout.setGeometry(QtCore.QRect(780, 400, 91, 21))
        self.btn_Logout.setMouseTracking(True)
        self.btn_Logout.setTabletTracking(True)
        self.btn_Logout.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                      "border-radius: 10px;\n"
                                      "font: 7pt \"Arial\";"
                                      "color: 'white';}" +
                                      "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Logout.setObjectName("pushButton_4")


        '''-----------Bottone pubblica----------'''

        self.btn_Pubblica = QtWidgets.QPushButton(Form)
        self.btn_Pubblica.setGeometry(QtCore.QRect(780, 350, 91, 21))
        self.btn_Pubblica.setMouseTracking(True)
        self.btn_Pubblica.setTabletTracking(True)
        self.btn_Pubblica.setStyleSheet("*{border: 2px solid rgb(18, 110, 60);"
                                        "border-radius: 10px;\n"
                                        "font: 7pt \"Arial\";"
                                        "color: 'white';}" +
                                        "*:hover{background: rgb(18, 110, 60);\n}")
        self.btn_Pubblica.setObjectName("pushButton_2")


        '''-----------Bottone limone (Easter egg)---------'''

        self.btn_limone = QtWidgets.QPushButton(Form)
        self.btn_limone.setGeometry(QtCore.QRect(790, 435, 70, 77))
        font = QtGui.QFont()
        self.btn_limone.setFont(font)
        self.btn_limone.setStyleSheet("*{border: 0.5px solid rgb(40, 39, 39);"
                                      "border-radius: 25px;\n"
                                      "font: 10pt \"Arial\";"
                                      "color: 'white';}")
        self.btn_limone.setText("")
        self.btn_limone.setObjectName("btn_limone")
        self.btn_limone.setIcon(QIcon('Limone.png'))
        self.btn_limone.setIconSize(QtCore.QSize(120, 120))


        '''------------Scritta "Playlist"-------------'''
        self.label_coming = QtWidgets.QLabel(Form)
        self.label_coming.setGeometry(QtCore.QRect(609, 305, 100, 30))
        self.label_coming.setStyleSheet("background-color: rgb(51, 51, 51);"
                                        "color: rgb(255, 252, 252);\n"
                                        "font: 10pt \".AppleSystemUIFont\";")
        self.label_coming.setObjectName("label_coming")


        '''------------GIF Coming soon----------'''

        self.centralwidget = QtWidgets.QWidget(Form)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setGeometry(QtCore.QRect(577, 330, 120, 120))
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
        self.txt_nome.setPlaceholderText(_translate("Form", "  Search..."))
        self.label.setText(_translate("Form", "PyLemon artista"))
        self.btn_mostraTutte.setText(_translate("Form", ""))
        self.btn_Impostazioni.setText(_translate("Form", "Impostazioni"))
        self.btn_Logout.setText(_translate("Form", "Log out"))
        self.btn_Pubblica.setText(_translate("Form", "Pubblica"))
        self.btn_search.setText(_translate("Form", ""))
        self.btn_limone.setText(_translate("Form", ""))
        self.label_coming.setText(_translate("Form", "Playlist"))

        item = self.table_top.horizontalHeaderItem(0)
        item.setText(_translate("Form", ""))
        font1 = QtGui.QFont().bold()
        font = QtGui.QFont("Arial", 10, font1)
        item.setFont(font)
        self.table_top.setColumnWidth(0, 191)
        self.label_2.setText(_translate("Form", "  TOP 5"))



        item = self.table_brani.horizontalHeaderItem(0)
        item.setText(_translate("Form", "I TUOI BRANI "))
        font1 = QtGui.QFont().bold()
        font = QtGui.QFont("Arial", 10, font1)
        item.setFont(font)
        self.table_brani.setColumnWidth(0, 231)
        self.label_3.setText(_translate("Form", "  I TUOI BRANI"))