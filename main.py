import sys
from PyQt5.QtWidgets import QApplication

from tkinter import *
from tkinter import filedialog
from pygame import *
import pygame
import threading
import os
import tkinter.ttk as ttk
from multiprocessing import Process


#---------> import delle classi <-------------


from Player.lettore import MusicPlayer


if __name__=='__main__':
	root = Tk()
	app= MusicPlayer(root)
	barThread = threading.Thread(target=1, args=(1,))
	# set thread as daemon (thread will die if parent is killed)
	barThread.daemon=True
	# Start thread, could also use root.after(50, barThread.start()) if desired
	barThread.start()
	root.mainloop()
