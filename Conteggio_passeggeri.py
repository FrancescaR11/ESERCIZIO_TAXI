#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:49:30 2020

@author: francescaronci
"""
from datetime import datetime
import pandas as pd

'''
Creo la funzione count_passengers_hours che prende in ingresso df_merged, DataFrame ottenuto con il merge dei due DataFrame di input,
la lista di boroughs e l'array "vettore_temporale" contenente le fasce orarie espresse in secondi. Questa funzione restituisce df_passeggeri, DataFrame 
contenente come colonne i nomi dei boroughs e come righe le fasce orarie ed il numero di passeggeri corrispondenti.
df_merged viene utilizzato per creare i sotto DataFrame relativi ai singoli borough, estratti dalla lista "boroughs", su cui, utilizzando il comando loc, individuiamo il 
numero di passeggeri per ciasciuna fascia oraria.
Il vettore temporale viene utilizzato per creare la lista di fasce orarie, che sarà utilizzata come index di df_passeggeri.

'''


# Creo funzione per il conteggio dei passeggeri per ogni fascia oraria ed ogni borough

def count_passengers_hour(df_merged,boroughs,vettore_temporale):
    
    #Imposto una data ed un'ora di riferimento
    ora_riferimento=datetime.timestamp(datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    
    #Creo un DataFrame vuoto che conterrà come index le fasce orarie e  come colonne il numero di passeggeri per ogni borough
    df_passeggeri=pd.DataFrame(0,columns=boroughs, index=list(range(0,23)) )
    
    
    for borough in boroughs: # Scandisco i borough uno alla volta
        
        df_merged_b=df_merged.loc[(df_merged['Borough'] == borough)] #Estraggo dal DataFrame un sotto DataFrame relativo al borough considerato
          
        fasce_orarie=[] # Inizializzo lista vuota, che conterrà le fasce orarie
        
        for j in range(len(vettore_temporale)-1): # Scandisco la lista vettore temporale contenete le fasce orarie espresse in secondi
            
                #Creo il vettore delle fasce orarie
                
                fasce_orarie.append(str(vettore_temporale[j]/3600)+'0' + '-' +str(vettore_temporale[j+1]/3600)+'0') # Creo la lista contenente le fasce orarie 
                
                '''
                    
                Calcolo la differenza in secondi tra la corsa i-esima e l'ora di riferimento. 
                Se questo valore cade nell'intervallo definito da due elementi del vettore_temporale,
                ovvero in una fascia oraria, aggiungo, nella colonna di df_passeggeri relativa al borough considerato,
                la somma dei passeggeri relativa alla fascia oraria in esame.
                    
                '''
                
                # Mi restringo al sotto DataFrame relativo ad una specifica fascia oraria
                
                df_2=df_merged_b.loc[(df_merged_b['Inizio Corsa']-ora_riferimento>=vettore_temporale[j]) & (df_merged_b['Inizio Corsa']-ora_riferimento<vettore_temporale[j+1])]
               
                
                #Inserisco nel DataFrame di output la somma dei passeggeri della singola fascia oraria
                        
                df_passeggeri.loc[j,borough] =  df_2['passenger_count'].sum()      

       
    df_passeggeri['indici']=fasce_orarie #Aggiungo 'fasce_orarie' come colonna al DataFrame di output 
        
    df_passeggeri.index=fasce_orarie # Imposto come index fasce_orarie
        
    del df_passeggeri['indici'] # Elimino  colonna contenente fasce_orarie
                   
    return df_passeggeri # Restituisco df_passeggeri

'''

Creo la funzione count_max_passengers, che restituisce il massimo numero di passeggeri ottenuto tra tutti i boroughs e tra tutte le fasce orarie,
prendendo in ingresso la lista di boroughs e df_passeggeri, DataFrame restituito dalla funzione count_passengers_hour. 
Questa funzione ha lo scopo di riprodurre in scala il grafico contenente i subplot per ogni borough.

'''
  

def count_max_passengers(boroughs,df_passeggeri):
    
    massimi=[] # Inizializzo lista vuota, che conterrà i massimi per ogni colonna
        
    for k in range(len(boroughs)): 
     
      massimi.append(max(df_passeggeri[boroughs[k]])) # Calcolo il massimo per ogni borough
      
      massimo=max(massimi)   # Calcolo il massimo tra i massimi di ogni borough
   
    return massimo # Restituisco il valore massimo da impostare come limite dell'asse y per il plot




