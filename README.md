# ESERCIZIO_TAXI

Il software si propone di svolgere un'analisi dei taxi a New York, rispondendo alla seguente specifica:
quali sono le fasce orarie con più passeggeri? E quella con meno? Impostate le vostre fasce orarie (per esempio ogni ora) e scoprite quali sono quelle in cui i taxi guidano il maggior numero di passeggeri e ripetete l'analisi per ogni borough. Fornite i risultati attraverso un plot.

Una volta effettuato il clone della repository, è necessario eseguire il file TAXI_CON_CLASSI.py, il quale, servendosi degli altri script presenti nella repository (Eliminazione_Nan, Conteggio_passeggeri, Conversion_timestamp) restituirà il plot richiesto dalla specifica. All'interno della repository git, è inoltre presente lo script estrazione_file_ridotto.py, utilizzato per estrarre dal file di input originario, presente solamente nella repository locale a causa delle elevate dimensioni, le ultime 200000 righe. Il file ridotto estratto dal file originario di input viene salvato nella cartella dati_ridotti, utilizzata per la lettura del file di input in TAXI_CON_CLASSI.py.
Per leggere i file di input originari, relativi a più mesi, occorre specificare da linea di comando la cartella 'dati', anzichè 'dati_ridotti'.

Il programma per funzionare si avvale di alcune dipendenze ed è quindi necessario importare i seguenti moduli:
-pandas
-numpy
-matplotlib 
-os
Inoltre l'importazione di 'tqdm' permette all'utente di visualizzare la percentuale di dati già esaminata tramite una barra di avanzamento durante l'esecuzione.
