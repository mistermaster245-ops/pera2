# Progetto informatica per le biotecnologie: Editing Genomico

**Autore:** Leonardo Mastrangeli

Questo programma serve a modellare e verificare l'inserimento di sequenze nucleotidiche 
(insertions) all'interno di un genoma base, controllando se l'operazione è avvenuta 
correttamente o se ci sono errori (mutazioni).

## Struttura del Progetto

Il codice è organizzato in due file per separare la logica
dai dati su cui in seguito viene eseguita tale logica.

### 1. Modulo `tools.py`
Questo file svolge le funzioni di calcolo. Contiene le funzioni che vengono importate e usate dal main:
* **`analizza(...)`**: È la funzione principale. Dato un genoma, un punto di inserimento 
e la sequenza che vogliamo inserire, calcola se l'edit avvenuto è corretto, quanti errori 
ci sono e dove è avvenuto il taglio.
* **`conta_errori(...)`**: Funzione che confronta due stringhe e conta quante lettere 
sono diverse.
* **`metti_spazi(...)`**: Funzione che serve solo per l'output. Prende la stringa finale e 
aggiunge degli spazi visivi prima e dopo l'inserimento per rendere più leggibile il risultato.

### 2. Modulo `main.py`
Questo è il file eseguibile. Contiene tutti gli esempi richiesti dalla traccia:
* **Parte A1**: Esegue l'analisi di due edit specifici (Edit 1 e Edit 2).
* **Parte A2**: Analizza una serie di inserimenti in diversi insertion points, e stampa 
la classifica finale degli scenari ordinata per numero di errori (dal migliore al peggiore).

## Quickstart

Per eseguire gli esempi di utilizzo richiesti dalla consegna, utilizzare il comando:

```bash
python main.py
