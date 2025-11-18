from moduli.gestorematrice import GestoreMatrice

# La classe ElaboratoreStatistico eredita da GestoreMatrice
class ElaboratoreStatistico(GestoreMatrice):
    def __init__(self, dati):  # dati sarà una lista di liste (la matrice)
        self.dati = dati       # salvo la matrice come attributo dell'oggetto

    # Metodo per trovare il valore massimo nella matrice
    def trova_massimo(self):
        massimo = self.dati[0][0]   # inizializzo il massimo con il primo elemento
        for riga in self.dati:      # scorro ogni riga della matrice
            for elemento in riga:   # scorro ogni elemento della riga
                if elemento > massimo:  # se trovo un elemento più grande
                    massimo = elemento   # aggiorno il massimo
        return massimo               # restituisco il massimo trovato

    # Metodo per calcolare la media di una riga specifica
    def media_riga(self, indice_riga):
        # controllo che l'indice sia valido (compreso tra 0 e numero righe - 1)
        if 0 <= indice_riga < len(self.dati):
            riga = self.dati[indice_riga]  # prendo la riga corrispondente
            
            somma = 0       # variabile per sommare gli elementi
            contatore = 0   # variabile per contare quanti elementi ci sono
            
            # scorro ogni elemento della riga
            for elemento in riga:
                somma = somma + elemento    # aggiungo l'elemento alla somma
                contatore = contatore + 1   # incremento il contatore
            
            media = somma / contatore       # calcolo la media
            return media                    # restituisco la media
        else:
            return None  # se l'indice non è valido, restituisco None
