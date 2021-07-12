import pygame
from pygame import mixer

'''classe relativa alla riproduzione musicale'''
class Ascolto():

    '''Nel costruttore si inizializzazano e si assegnano gli attributi responsabii del corretto funzionanmento della riproduzione'''
    def __init__(self):
        self.path_riproduzione = ''
        self.check_pause = True
        self.path_selezione = ''
        pygame.init()


    '''Metodo che in base al percorso file del brano e al volume che l'utente ha selezionato,
       avvia la classe mixer di pygame quindi la riproduzione'''
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


    '''Metodo che mette in pausa il flusso musicale'''
    def pause(self):
        mixer.music.pause()
        self.check_pause = False

    '''Metodo che stoppa il flusso musicale'''
    def stop(self, bool_finestra):
        if bool_finestra:
            if mixer.music.get_busy():
                mixer.music.stop()
                self.check_pause = True
                mixer.quit()

        else:
            mixer.music.stop()
            self.check_pause = True


    '''Metodo che regola il volume della riproduzione musicale ogni qual volta l'utente cambi la posizione dello slider'''
    def vol_adjust(self,valore):
        mixer.music.set_volume(float(valore/10))
