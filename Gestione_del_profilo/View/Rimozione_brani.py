
from PyQt5 import QtCore, QtGui, QtWidgets


'''--------------Classe view eliminazione brano----------'''

class rimozione_brani(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 491)
        Form.setMinimumSize(QtCore.QSize(521, 491))
        Form.setMaximumSize(QtCore.QSize(521, 491))
        Form.setStyleSheet("background-color: rgb(40, 39, 39);")


        '''---------Titolo finestra---------'''

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(180, 18, 170, 60))
        self.label.setStyleSheet("color: rgb(221, 215, 25);\n"
                                 "font: 25pt \".AppleSystemUIFont\";")
        self.label.setObjectName("label")


        '''--------Sottotitolo--------'''

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(205, 70, 131, 21))
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.label_2.setObjectName("label_2")


        '''-----------Tabella contenente i brani da selezionare per poterli eliminare----------'''

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setGeometry(QtCore.QRect(40, 110, 441, 281))
        self.table.setMinimumSize(QtCore.QSize(3, 0))
        self.table.setMouseTracking(False)
        self.table.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                       "background-color: rgb(51, 51, 51);"
                                       "border-radius: 5px;\n"
                                       "font: 10pt;"
                                       "color: 'white';}")
        self.table.setObjectName("tableWidget")

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


        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(40, 110, 441, 30))
        self.label_4.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                   "background-color: rgb(51, 51, 51);"
                                   "border-radius: 5px;\n"
                                   "color: 'white';}")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")



        '''-----------Informativa per l'utente in basso alla finestra-----------'''

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(130, 460, 291, 21))
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);\n")
        self.label_3.setObjectName("label_3")


        '''-----------Tasto eliminazione----------'''

        self.btn_eliminazione = QtWidgets.QPushButton(Form)
        self.btn_eliminazione.setGeometry(QtCore.QRect(300, 420, 81, 21))
        self.btn_eliminazione.setObjectName("pushButton")
        self.btn_eliminazione.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                            "border-radius: 10px;\n"
                                            "color: 'white';}" +
                                            "*:hover{background: rgb(221, 215, 25);\n}")


        '''-----------Tasto indietro-----------'''

        self.btn_Back = QtWidgets.QPushButton(Form)
        self.btn_Back.setGeometry(QtCore.QRect(150, 420, 81, 21))
        self.btn_Back.setMouseTracking(True)
        self.btn_Back.setTabletTracking(True)
        self.btn_Back.setStyleSheet("*{border: 0.5px solid rgb(221, 215, 25);"
                                    "border-radius: 10px;\n"
                                    "color: 'white';}" +
                                    "*:hover{background: rgb(221, 215, 25);\n}")
        self.btn_Back.setObjectName("pushButton_3")



        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", ""))
        self.label.setText(_translate("Form", "PyLemon"))
        self.label_2.setText(_translate("Form", "Eliminazione brano"))
        self.label_3.setText(_translate("Form", "(Prima di premere elimina seleziona un brano)"))
        self.btn_eliminazione.setText(_translate("Form", "Elimina"))
        self.btn_Back.setText(_translate("Form", "Indietro"))
        self.label_4.setText(_translate("Player", "I TUOI BRANI"))

        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", ""))
        font1 = QtGui.QFont().bold()
        font = QtGui.QFont("Arial", 10, font1)
        item.setFont(font)
        self.table.setColumnWidth(0, 441)
