class GestoreMatrice: #Creo la classe GestoreMatrice
    def __init__(self, dati): #Dati sarà una lista di liste
        self.dati = dati
        
def stampa_matrice(self):
        if not self.valida_matrice():#Controllo se la matrice è valida
            print("Matrice non valida!")
            return

        for riga in self.dati: #Per ogni riga della matrice converto gli elementi in stringa
            riga_formattata = "\t".join(str(x) for x in riga)
            print(riga_formattata)
            
def valida_matrice(self):
    if not self.dati:#Controllo se la matrice è vuota
        return False 

    lunghezza = len(self.dati[0]) #Controllo la lunghezza di ogni riga
    for riga in self.dati:
        if len(riga) != lunghezza:
            return False
    return True