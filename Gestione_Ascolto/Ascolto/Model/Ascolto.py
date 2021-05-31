import os

import pygame
from pygame import mixer
#import pygame

class Ascolto():
    def __init__(self):
        self.path_riproduzione = ''
        #self.playState = False
        self.check_pause = True
        self.path_selezione = ''
        '''self.check_prev = False
        self.check_next = False'''
        pygame.init()

    def play(self, path, volume): #passo da vistaAscolto o da CobntrolloreAscolto? curseselection()
        if self.path_selezione != path:
            self.check_pause = True
            #self.path_selezione = path
        if self.check_pause:
            mixer.init()
            mixer.music.load(path)
            mixer.music.set_volume(volume)
            self.path_selezione = path
            mixer.music.play()
        else:
            mixer.music.unpause()
            #self.playState = True



    def pause(self):
        #if self.playState:
        mixer.music.pause()  # pausa se flusso musicale attivo
            #self.playState = False
        self.check_pause = False
        '''else:
            mixer.music.unpause() # riprendi se flusso musicale prima "pausato"
            self.playState = False'''

    def stop(self):
        mixer.music.stop()
        self.check_pause = True
        #self.playState = False

    def vol_adjust(self,valore):
        mixer.music.set_volume(float(valore/10))


    #per il prev e next richiami play cambiando path!!!;
    #controllo posizione etc fai in vista