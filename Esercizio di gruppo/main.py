from moduli.elaboratore_statistico import ElaboratoreStatistico as es
from moduli.gestorematrice import GestoreMatrice as gm
from moduli.elaboratore_matematico import ElaboratoreMatematico as em
from moduli.filtromatrice import FiltroMatrice as fm

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
        gm.stampa_matrice(matrice)
    elif scelta == "2":
        gm.valida_matrice(matrice)
        
    elif scelta == "3":
        es.trova_massimo(matrice)
    elif scelta == "4":
        es.media_riga(matrice)
    elif scelta == "5":
        fm.azzera_negativi(matrice)

    elif scelta == "6":
        fm.appiattisci(matrice)

    elif scelta == "7":
        em.trasponi(matrice)
        
    elif scelta == "8":
        em.moltiplica_per_scalare(matrice)

    elif scelta == "0":
        print("Uscita dal programma...")
        break

    else:
        print("Scelta non valida, riprova.")