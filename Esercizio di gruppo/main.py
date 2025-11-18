from moduli.elaboratore_statistico import ElaboratoreStatistico
from moduli.gestorematrice import GestoreMatrice , stampa_matrice, valida_matrice
from moduli.elaboratoreMatematico import ElaboratoreMatematico
from moduli.filtromatrice import FiltroMatrice

matrice = [
    [12, 7, 5, 3],
    [9, 15, 6, 2],
    [4, 8, 10, 1],
    [11, 13, 7, 0],
    [6, 14, 9, 5]
]



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

    scelta = input("Seleziona un'opzione: ")

    if scelta == "1":
        stampa_matrice(matrice)

    elif scelta == "2":
        valida_matrice()
        
    elif scelta == "3":
        pass
    elif scelta == "4":
       
        pass
    elif scelta == "5":
        # se hai la classe FiltroMatrice
        pass

    elif scelta == "6":
        # se hai la classe FiltroMatrice
        pass

    elif scelta == "7":
        # se hai la classe ElaboratoreMatematico
        pass

    elif scelta == "8":
        # se hai la classe ElaboratoreMatematico
        pass

    elif scelta == "0":
        print("Uscita dal programma...")
        break

    else:
        print("Scelta non valida, riprova.")