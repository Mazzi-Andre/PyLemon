from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

from Gestione_Ascolto.Ascolto.Controller.ControlloreAscolto import ControlloreAscolto
from Gestione_Ascolto.Ascolto.Model.Ascolto import Ascolto


'''Classe relativa alla vista grafica del Player, quindi dei dati presenti nella piattaforma'''
class Ui_Player(object):
    def setupUi(self, Player):
        self.listen = Ascolto()
        self.controller = ControlloreAscolto()
        self.search = False
        Player.setObjectName("Player")
        Player.resize(501, 471)
        Player.setAutoFillBackground(False)
        Player.setStyleSheet("background-color: rgb(40, 39, 39);\n""\n""")
        self.table = QtWidgets.QTableWidget(Player)
        self.table.setGeometry(QtCore.QRect(0, 0, 501, 351))
        self.table.setMinimumSize(QtCore.QSize(3, 0))
        self.table.setMouseTracking(False)
        self.table.setStyleSheet("background-color: rgb(207, 207, 207);\n""")
        self.table.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.table.setLineWidth(0)
        self.table.setMidLineWidth(0)
        self.table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.table.setAutoScroll(False)
        self.table.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.SelectedClicked)
        self.table.setDragDropOverwriteMode(False)
        self.table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.table.setShowGrid(False)
        self.table.setGridStyle(QtCore.Qt.NoPen)
        self.table.setObjectName("table")
        self.table.setColumnCount(3)

        item = QtWidgets.QTableWidgetItem();item.setTextAlignment(QtCore.Qt.AlignCenter)
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
        self.table.verticalHeader().setVisible(True)
        self.table.verticalHeader().setHighlightSections(True)

        self.play = QtWidgets.QPushButton(Player)
        self.play.setGeometry(QtCore.QRect(10, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.play.setFont(font)
        self.play.setStyleSheet("font color : rgb (255, 255, 0)\n""border-radius: 10px;")
        self.play.setText("")
        self.play.setObjectName("play")
        self.play.setIcon(QIcon('play.png'))


        self.pause = QtWidgets.QPushButton(Player)
        self.pause.setGeometry(QtCore.QRect(110, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.pause.setFont(font)
        self.pause.setStyleSheet("font color:rgb (255,255,0)\n""border-radius: 10px;")
        self.pause.setText("")
        self.pause.setObjectName("pause")
        self.pause.setIcon(QIcon('pause.png'))


        self.stop = QtWidgets.QPushButton(Player)
        self.stop.setGeometry(QtCore.QRect(210, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.stop.setFont(font)
        self.stop.setStyleSheet("font color:rgb (255,255,0)\n""border-radius: 10px;")
        self.stop.setText("")
        self.stop.setObjectName("stop")
        self.stop.setIcon(QIcon('stop.png'))


        self.prev = QtWidgets.QPushButton(Player)
        self.prev.setGeometry(QtCore.QRect(310, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setFont(font)
        self.prev.setStyleSheet("font color:rgb (255,255,0)\n""border-radius: 10px;")
        self.prev.setText("")
        self.prev.setObjectName("prev")


        self.next = QtWidgets.QPushButton(Player)
        self.next.setGeometry(QtCore.QRect(410, 370, 81, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.prev.setIcon(QIcon('prev.png'))
        self.next.setFont(font)
        self.next.setStyleSheet("font color:rgb (255,255,0)\n""border-radius: 10px;")
        self.next.setText("")
        self.next.setObjectName("next")
        self.next.setIcon(QIcon('next.png'))


        self.horizontalSlider = QtWidgets.QSlider(Player)
        self.horizontalSlider.setGeometry(QtCore.QRect(70, 440, 90, 16))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        #self.horizontalSlider.setStyleSheet("QSlider::handle:horizontal {background-color: white;}")
        self.horizontalSlider.setRange(0,10)
        self.horizontalSlider.setValue(2)


        self.label = QtWidgets.QLabel(Player)
        self.label.setGeometry(QtCore.QRect(13, 438, 55, 16))
        self.label.setStyleSheet("QLabel { color : white; }");
        self.label.setObjectName("label")

        self.retranslateUi(Player)
        QtCore.QMetaObject.connectSlotsByName(Player)

    def retranslateUi(self, Player):
        _translate = QtCore.QCoreApplication.translate
        Player.setWindowTitle(_translate("Player", "Player"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Player", "Titolo"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Player", "Album"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Player", "Artista"))
        self.table.setColumnWidth(0, 167);
        self.table.setColumnWidth(1, 167) ;
        self.table.setColumnWidth(2, 167)
        self.label.setText(_translate("Player", "Volume"))


