import pygame
from pygame import mixer

class Ascolto():
    def __init__(self):
        self.path_riproduzione = ''
        self.check_pause = True
        self.path_selezione = ''
        pygame.init()

    def play(self, path, volume):
        if self.path_selezione != path:
            self.check_pause = True
        if self.check_pause:
            mixer.init()
            mixer.music.load(path)
            mixer.music.set_volume(volume)
            self.path_selezione = path
            mixer.music.play()
        else:
            mixer.music.unpause()



    def pause(self):
        mixer.music.pause()
        self.check_pause = False

    def stop(self):
        mixer.music.stop()
        self.check_pause = True
        #self.playState = False

    def vol_adjust(self,valore):
        mixer.music.set_volume(float(valore/10))