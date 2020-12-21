#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:49:30 2020

@author: francescaronci
"""
from datetime import datetime
import pandas as pd



# Creo funzione per il conteggio dei passeggeri per ogni fascia oraria ed ogni borough

def count_passengers_hour(df_merged,boroughs,vettore_temporale):
    
    #Imposto una data ed un'ora di riferimento
    ora_riferimento=datetime.timestamp(datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    
    #Creo un DataFrame vuoto che conterrà come index le fasce orarie e  come colonne il numero di passeggeri per ogni borough
    df_passeggeri=pd.DataFrame()
    
    
    for borough in boroughs:
        df_merged_b=df_merged.loc[(df_merged['Borough'] == borough)] #Estraggo dal DataFrame un sotto DataFrame relativo al borough considerato
          
        #Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista   
        
        numero_passeggeri=[]
        fasce_orarie=[]
        
        for j in range(len(vettore_temporale)-1):
                
                passeggeri=0 # Inizializzo il numero di passeggeri con il valore zero
                
                fasce_orarie.append(str(vettore_temporale[j]/3600)+'0' + '-' +str(vettore_temporale[j+1]/3600)+'0') # Creo la lista contenente le fasce orarie 
                
                for i in list(df_merged_b.index)[0:1000]: # Mi restringo ad un sotto DataFrame per velocizzare l'esecuzione
                
                    '''
                    
                    Calcolo la differenza in seocondi tra la corsa i-esima e l'ora di riferimento. 
                     Se questo valore cade nell'intervallo definito da due elementi del vettore_temporale,
                    ovvero in una fascia oraria, aggiungo a passeggeri il numero di passeggeri di quella corsa
                    
                    '''
                    
                    if vettore_temporale[j]<(abs(df_merged_b['Inizio Corsa'][i]-ora_riferimento))<vettore_temporale[j+1]:
                        
                        
                         passeggeri+=int(df_merged_b['passenger_count'][i])    

                
                numero_passeggeri.append(passeggeri)
       
        df_passeggeri['indici']=fasce_orarie #Aggiungo 'fasce_orarie' come colonna al DataFrame di output e lo imposto come index
        
        df_passeggeri.index=fasce_orarie
        
        del df_passeggeri['indici'] 
        
        df_passeggeri[borough]=numero_passeggeri # Aggiungo la colonna relativa al borough con il numero dei passeggeri
    
    return df_passeggeri



# Creo la funzione che calcola il massimo numero di passeggeri ottenuto tra tutti i boroughs e tra tutte le fasce orarie   

def count_max_passengers(boroughs,df_passeggeri):
    
    massimi=[]
        
    for k in range(len(boroughs)):
     
      massimi.append(max(df_passeggeri[boroughs[k]])) # Calcolo il massimo per ogni borough
      
      massimo=max(massimi)   # Calcolo il massimo tra i massimi di ogni borough
   
    return massimo # Restituisco il valore massimo da impostare come limite dell'asse y per il plot








