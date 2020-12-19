#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:49:30 2020

@author: francescaronci
"""
from datetime import datetime
import pandas as pd

def count_passengers_hour(df_merged,boroughs,fasce_orarie):
    #imposto una data di riferimento
    
    ora_riferimento=datetime.timestamp(datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    
    df_passeggeri=pd.DataFrame()
    
    for borough in boroughs:
        df_merged_b=df_merged.loc[(df_merged['Borough'] == borough)]
          
        #Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista   
        numero_passeggeri=[]
        orari=[]
        for j in range(len(fasce_orarie)-1):
                passeggeri=0
                orari.append(str(fasce_orarie[j]/3600)+'0' + '-' +str(fasce_orarie[j+1]/3600)+'0')
                
                for i in list(df_merged_b.index)[0:1000]:
                    
                    #tutte le corse che cadono dalle 00:00 alle 01:00 e così via
                    if fasce_orarie[j]<(abs(df_merged_b['Inizio Corsa'][i]-ora_riferimento))<fasce_orarie[j+1]:
                        
                         
                        
                        
                        
                         passeggero=int(df_merged_b['passenger_count'][i])    
                         passeggeri+=passeggero
                numero_passeggeri.append(passeggeri)
        df_passeggeri['indici']=orari
        df_passeggeri.index=orari
        del df_passeggeri['indici']
        df_passeggeri[borough]=numero_passeggeri
    
    return df_passeggeri
    

def count_max_passengers(boroughs,df_passeggeri):
    massimi=[]
        
    for k in range(len(boroughs)):
      massimi.append(max(df_passeggeri[boroughs[k]]))
      massimo=max(massimi)  
    return massimo