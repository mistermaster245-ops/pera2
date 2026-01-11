from tools import analizza, metti_spazi
#importiamo le funzioni di cui abbiamo bisogno

def main():
    print("=== PROGETTO INFORMATICA PER LE BIOTECNOLOGIE DI LEONARDO MASTRANGELI ===\n")

#main e' la funzione cuore del progetto, e' quella che poi da' l'output. \n dice di andare a capo lasciando una riga vuota
    # --- PARTE A1 ---
    print("--- Parte A1 ---")
    genoma = "GATACAGATACA"
    insertion_point = "CA"
    insertion = "TTTT"

    print(f"Genoma: {genoma}")
    print(f"Insertion Point: {insertion_point}")
    print(f"Insertion: {insertion}")
    print("-" * 30)

    lista_edit_a1 = [
        "GATACATTTTGATACA",
        "GATACATATTGATACA"
    ]

    numero_edit = 1
    for edit in lista_edit_a1:
#edit variabile temporanea, prendeu n genoma dalla lista a ogni ciclo
        err, idx = analizza(genoma, insertion_point, insertion, edit)
#invochiamo la funzione analizza che ci restituisca err ed idx
        visivo = edit
        if idx != -1:
#controlla se l'analisi ha funzionato
            visivo = metti_spazi(edit, idx, len(genoma))
#invochiamo funzione che aggiunge gli spazi. se l'inserzione e' avvenuta e idx!=-1, aggiorna visivo al genoma editato con gli spazi
        print(f"Edit {numero_edit}: {visivo}")
#stampa la versione con gli spazi di edit 1 o 2
        if err == 0:
            print("Risultato: CORRETTO (0 errori)")
        elif err > 0:
            print(f"Risultato: INCORRETTO ({err} errori)")
        else:
            print("Risultato: Non compatibile")
#se non e' 0 ne' maggiore di 0, allora e' -1 e qualcosa e' andato storto
        print() #stampa una riga vuota cosi' risultato edit 1 e 2 sono staccati
        numero_edit += 1

    print("=" * 40 + "\n")
#moltiplico = 40 volte e poi vado a capo saltando una riga

    # --- PARTE A2 ---
    print("--- Parte A2 ---")

    genoma2 = "CGGCATAACGGC"

    lista_punti = ["TA", "GC"]
    lista_insertions = ["AAA", "CCC"]

#Scenari: accoppiamo il primo punto con la prima inserzione, ecc.
    scenari = [
        ("TA", "AAA"),
        ("GC", "CCC")
    ]
#TA deve stare con AAA, GC con CCC, tuple
    print(f"Genoma: {genoma2}")
    print(f"Insertion Points: {lista_punti}")
    print(f"Insertions: {lista_insertions}")
    print("\nCLASSIFICA FINALE:")
    print("-" * 40)

    lista_da_ordinare = [
        "CGGCATAAAAACGGC",
        "CGGCCCCATAACGGC",
        "CGGCATAAACACGGC",
        "CGGCTCCATAACGGC",
        "CGGCATAGGGACGGC"
    ]

    classifica = []

    for edit in lista_da_ordinare:
        best_err = 1000
        best_punto = ""
        best_idx = -1
#iniziamo il ciclo che analizza i vari edit partendo da 1000 errori cosi ogni errore minore e' preso
        for insertion_point, insertion in scenari:
            err, idx = analizza(genoma2, insertion_point, insertion, edit)
#analizza segue le regole di pair imposte dalle tuple
            if err != -1 and err < best_err:
                best_err = err
                best_punto = insertion_point
                best_idx = idx

        classifica.append((edit, best_err, best_punto, best_idx))
        """il programma testa l'uno e l'altro insertion nei rispettivi insertion points, 
        e quello che e' avvenuto davvero tra i due viene inserito nella lista classifica, 
        e questo si ripete per tutti i genomi editati nella lista da ordinare. tieni a mente
        che best_err fa riferimento al best_err di quello specifico edit (che se nulla e'
        andato storto sara' sempre minore di 1000), NON al minor errore in assoluto, che
        conosceremo in seguito grazie al sorting in base agli errori"""

    classifica.sort(key=lambda pera_check: pera_check[1])
    """operatore che ordina la classifica secondo il criterio di quanti errori ci sono. 
    lambda dice che e' una funzione temporanea che non va definita mentre pera check[1] 
    dice che nella classifica si vuole ordinare in base al parametro 1, cioe il numero di 
    errori"""

    posizione = 1

    #inizializza un contatore per scrivere 1, 2 e 3 davanti ai risultati
    for r in classifica:
        testo_editato, err, punto, idx = r

        if err == 1000:
            print(f"{posizione}. {testo_editato}, # Nessun match valido") #nessuno scenario e' avvenuto
        else:
            testo_spazi = metti_spazi(testo_editato, idx, len(genoma2))
            print(f"{posizione}. {testo_spazi}, # errori: {err} su insertion point {punto}")
#ciclo for finisce quando finiscono i genomi editati in classifica
        posizione += 1

main() #niente dentro alla parentesi perche' tutte le variabili del programma sono incluse in funzione main
