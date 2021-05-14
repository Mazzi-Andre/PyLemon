
from pygame import *

class Ascolto():
    def __init__(self):
        self.music_file = False # non mi dovrebbe servire (path)
        self.playState = False
        self.lst_pos = 1
        self.musicdirs = []
        mixer.init()

    def play(self, path): #passo da vistaAscolto o da CobntrolloreAscolto? curseselection()
        mixer.music.load(path)
        mixer.music.play()
        self.playState = True

    def pause(self):
        if not self.palyState:
            mixer.music.pause()  # pausa se flusso musicale attivo
            self.playState=False
        else:
            mixer.music.unpause() # riprendi se flusso musicale prima "pausato"
            self.playState = False

    def stop(self):
        mixer.music.stop()
        self.playState = False

    def prevSong(self, selezione):
        if selezione and self.playState == True:
            if

