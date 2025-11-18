from gestorematrice import GestoreMatrice

class ElaboratoreMatematico(GestoreMatrice):
    
    def trasponi(self):
        # Crea una nuova lista vuota che conterrà la matrice trasposta
        nuova_matrice = []
        
        # Cicla attraverso il numero di colonne della matrice originale
        for col in range(len(self.dati[0])):  
            nuova_riga = []  # Inizia una nuova riga trasposta
            
            # Per ogni riga della matrice originale, prendi l'elemento della colonna corrente
            for riga in self.dati:
                nuova_riga.append(riga[col])
            
            # Aggiungi la nuova riga alla matrice trasposta
            nuova_matrice.append(nuova_riga)

        # Restituisce la nuova matrice che è la trasposta della matrice originale
        return nuova_matrice 
                
            
    def moltiplica_per_scalare(self, k):
        # Crea una nuova matrice vuota che conterrà il risultato
        nuova_matrice = []
        
        # Scorre ogni riga della matrice originale
        for riga in self.dati:
            nuova_riga = []  # Crea una nuova riga modificata
            
            # Scorre ogni numero nella riga e lo moltiplica per lo scalare k
            for numero in riga:
                nuova_riga.append(numero * k)
            
            # Aggiungi la riga modificata alla nuova matrice
            nuova_matrice.append(nuova_riga)
            
        # Restituisce la nuova matrice scalata
        return nuova_matrice
