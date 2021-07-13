
'''Classe di controllo statistica to 5'''
class TopFive():

    '''Metodo che ritorna una lista ordinata in ordine decrescente contenente i valori degli ascolti di tutti i brani'''
    def sort_lista_contatori(self, json_data):
        lista_contatori = []
        j = 0
        for i in json_data:
            lista_contatori.append(i["contatore"])
            if j>0:
                if lista_contatori[j-1] == lista_contatori[j]:
                    lista_contatori.pop(j)
            if j<len(lista_contatori):
                j = j+1
        lista_contatori.sort()
        lista_contatori.reverse()

        return lista_contatori
