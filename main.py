"""
funzione che usiamo per contare quanti errori ci sono nella comparison
fra due insertions (la desiderata e la ottenuta). S1 ed S2 sono le due insertions
che stiamo analizzando.
"""
def conta_errori(s1, s2):
    if len(s1) != len(s2):
        return -1
#se le lunghezze sono diverse, il programma si ferma subito (no indel, solo puntiformi)
    errori = 0
    for i in range(len(s1)):
        """ range: Significato: "Per tutta la lunghezza".

Cosa fa davvero: "Mi dà i numeri di posizione (0, 1, 2...) uno alla volta"."""
        if s1[i] != s2[i]:
            errori += 1
    return errori
"""controllo base per base, per tutta la lunghezza di S1 ed S2, che S1 ed S2 coincidano; 
se una o piu basi sono diverse, ci sono stati uno o piu errori
nell'insertion desiderata e in quella ottenuta. infine la funzione ci restituisce
l'ammontare di errori rilevato"""



"""
questa altra funzione ha un ruolo estetico: per rendere piu chiaro il risultato,
inseriamo uno spazio prima e dopo l'insertion, come ha fatto lei, prof.
"""
def metti_spazi(testo, indice, lunghezza_totale):
    lunghezza_suffisso = lunghezza_totale - indice
#calcola quanto e' lunga la parte che succede al taglio
    fine_inserimento = len(testo) - lunghezza_suffisso
#calcola dove finisce l'inserimento sottraendo al genoma editato la lunghezza del suo suffisso
    pera1 = testo[:indice]
#prende cio' che c'e' prima del punto di taglio (prefisso)
    pera2 = testo[indice:fine_inserimento]
#prende l'insertion (start:end)
    pera3 = testo[fine_inserimento:]
#prende cio' che c'e' dopo l'insertion (suffisso)
    return f"{pera1} {pera2} {pera3}"
#la f string ci permettera' poi di printare il nostro genoma editato con gli spazi gia' inseriti qui.



"""questa funzione e' il cuore del mio progetto:"""
def analizza(genoma, punto, insertion, edit):
    if len(edit) != len(genoma) + len(insertion):
        return -1, -1
#se la lunghezza del genoma editato non e' lunghezza originale+inserzione, qualcosa e' andato molto male
#ci sono due -1 perche alla fine la funzione deve restituire non 1 ma ben 2 valori
    posizioni = []
    start = 0
    while True:
#ciclo infinito comodo per ripeterlo finche vogliamo
        trovato = genoma.find(punto, start)
#cerca il punto di inserzione dentro il genoma
        if trovato == -1:
            break
#se li abbiamo trovati tutti, stop
        taglio = trovato + len(punto)
#find trova l'inizio dell'insertion, ma noi dobbiamo tagliare alla fine; se insertion e' CA non dobbiamo tagliare dopo C, ma dopo CA, quindi bisogna aggiungerci lunghezza insertion point
        posizioni.append(taglio)
#mette il punto di taglio trovato nella lista posizioni
        start = trovato + 1
#spostiamo il punto di ricerca un po piu avanti per vedere se ce ne sono altri

    miglior_err = 1000
#appena troveremo un numero, quello diventera' il nuovo king of the hill, partiamo da 1000 per avere un numero a caso alto
    miglior_idx = -1
#se alla fine della ricerca non abbiamo trovato nessun punto valido, questa variabile rimarrà -1 e capiremo che l'operazione è fallita
    for p in posizioni:
        prefix = genoma[:p]
        suffix = genoma[p:]
#prendo le parti prima e dopo il punto di taglio
        if edit.startswith(prefix) and edit.endswith(suffix):
            parte_centrale = edit[len(prefix): len(edit) - len(suffix)] #(start:end, slicing)
#l'insertion e' l'edit senza il prefisso e il suffisso
            err = conta_errori(insertion, parte_centrale) #invocazione funzione
#confronta l'insertion desiderato con quello che abbiamo effettivamente ottenuto
            if err < miglior_err:
                miglior_err = err
                miglior_idx = p
#se l'errore e' minore del minor error precedente, batte il record e diviene il minor numero di errori attuale

    if miglior_err == 1000:
        return -1, -1
#se non ci sono stati match, qualcosa e' nuovamente andato storto
    return miglior_err, miglior_idx
#se invece tutto e' andato bene, la funzione restituisce il minor numero di errori e il rispettivo indice
