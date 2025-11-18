class GestoreMatrice:  # Creo la classe GestoreMatrice
    def __init__(self, dati):  # dati sarà una lista di liste (la matrice)
        self.dati = dati

    def stampa_matrice(self):
        # Controllo se la matrice è valida
        if not self.valida_matrice():
            print("Matrice non valida!")
            return

        # Per ogni riga della matrice converto gli elementi in stringa
        for riga in self.dati:
            riga_formattata = "\t".join(str(x) for x in riga)
            print(riga_formattata)

    def valida_matrice(self):
        # Controllo se la matrice è vuota
        if not self.dati:
            return False

        # Controllo che tutte le righe abbiano la stessa lunghezza
        lunghezza = len(self.dati[0])
        for riga in self.dati:
            if len(riga) != lunghezza:
                return False
        return True
