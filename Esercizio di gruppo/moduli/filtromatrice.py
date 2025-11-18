from moduli.gestorematrice import GestoreMatrice

class FiltroMatrice(GestoreMatrice):

    def azzera_negativi(self):
        for i in range(len(self.dati)): #Scorro gli indici delle righe
            for j in range(len(self.dati[i])): #Scorro gli indici delle colonne
                if self.dati[i][j] < 0: #Se il valore nella cella è negativo lo sostituisco con 0
                    self.dati[i][j] = 0

    def appiattisci(self):
        lista_appiattita = [] #Creo una lista vuota che conterrà tutti i numeri
        for riga in self.dati: #Scorro ogni riga
            for valore in riga: #Scorro ogni numero della riga
                lista_appiattita.append(valore) #Aggiungo ogni numero alla lista
        return lista_appiattita #Restitisco la lista finale
