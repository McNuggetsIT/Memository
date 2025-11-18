# Importo le classi dai moduli
from moduli.elaboratore_statistico import ElaboratoreStatistico
from moduli.gestorematrice import GestoreMatrice
from moduli.elaboratore_matematico import ElaboratoreMatematico
from moduli.filtromatrice import FiltroMatrice

# Definisco la matrice di partenza (lista di liste)
matrice = [
    [12, 7, 5, 3],
    [9, 15, 6, 2],
    [4, 8, 10, 1],
    [11, 13, 7, 0],
    [6, 14, 9, 5]
]

# Creo gli oggetti delle varie classi passando la matrice
gm = GestoreMatrice(matrice)          # Gestione base della matrice
es = ElaboratoreStatistico(matrice)   # Operazioni statistiche
em = ElaboratoreMatematico(matrice)   # Operazioni matematiche
fm = FiltroMatrice(matrice)           # Operazioni di filtro

# Ciclo infinito per il menu interattivo
while True:
    print("\n--- MENU ---")
    print("1: Stampa Matrice")
    print("2: Valida Matrice")
    print("3: Trova Massimo")
    print("4: Media Riga")
    print("5: Azzera Negativi")
    print("6: Appiattisci")
    print("7: Trasponi")
    print("8: Moltiplica per Scalare")
    print("0: Esci")

    # L'utente inserisce la scelta
    scelta = input("Seleziona un'opzione: ")

    # Stampa la matrice
    if scelta == "1":
        gm.stampa_matrice()

    # Controlla se la matrice è valida (righe della stessa lunghezza)
    elif scelta == "2":
        print("Matrice valida?", gm.valida_matrice())

    # Trova il valore massimo nella matrice
    elif scelta == "3":
        print("Massimo:", es.trova_massimo())

    # Calcola la media di una riga specifica
    elif scelta == "4":
        indice = int(input("Inserisci indice riga (0-based): "))
        print("Media riga:", es.media_riga(indice))

    # Sostituisce i valori negativi con 0
    elif scelta == "5":
        nuova = fm.azzera_negativi()
        for riga in nuova:
            print(riga)

    # Appiattisce la matrice in una lista unica
    elif scelta == "6":
        print(fm.appiattisci())

    # Trasposta la matrice (righe <-> colonne)
    elif scelta == "7":
        trasposta = em.trasponi()
        for riga in trasposta:
            print(riga)

    # Moltiplica tutti gli elementi della matrice per uno scalare k
    elif scelta == "8":
        k = int(input("Inserisci scalare: "))
        scalata = em.moltiplica_per_scalare(k)
        for riga in scalata:
            print(riga)

    # Esce dal programma
    elif scelta == "0":
        print("Uscita dal programma...")
        break

    # Gestione di input non validi
    else:
        print("Scelta non valida, riprova.")
