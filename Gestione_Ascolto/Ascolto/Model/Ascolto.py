import os

import pygame
from pygame import mixer
#import pygame

class Ascolto():
    def __init__(self):
        self.music_file = False # non mi dovrebbe servire (path)
        self.playState = False
        self.lst_pos = 1
        self.musicdirs = []
        pygame.init()

    def play(self, path): #passo da vistaAscolto o da CobntrolloreAscolto? curseselection()
        if not self.playState:
            mixer.music.unpause()
            self.playState = True
        else:
            mixer.init()
            mixer.music.load(path)
            mixer.music.set_volume(0.7)
            mixer.music.play()
            self.playState = True

    def pause(self):
        if self.playState:
            mixer.music.pause()  # pausa se flusso musicale attivo
            self.playState = False
        '''else:
            mixer.music.unpause() # riprendi se flusso musicale prima "pausato"
            self.playState = False'''

    def stop(self):
        mixer.music.stop()
        self.playState = False


    def volup(self):
        pygame.mixer.music.set_volume(min(1.0,pygame.mixer.music.get_volume()+0.1))

    def voldown(self):
        pygame.mixer.music.set_volume(max(0.0,pygame.mixer.music.get_volume()-0.1))


    #per il prev e next richiami play cambiando path!!!;
    #controllo posizione etc fai in vista