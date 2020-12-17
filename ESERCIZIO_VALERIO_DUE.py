#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 10:32:43 2020

@author: francescaronci
"""
import time
import json
import pandas as pd
from numpy import var
import argparse
from datetime import datetime
import numpy as np
import sys
from Eliminazione_Nan import replace_Nan_with_zeros
from Conteggio_passeggeri import count_passengers_hour

'''
Uso argparse per la lettura dei file, con "i" che scandisce i mesi.
Se non è presente il file dell' i-esimo mese sollevo un eccezione che ci restituisce 'Il file non esiste' 
'''

i=1
df=pd.DataFrame()
while i in range(13):
 try:
     
       parser=argparse.ArgumentParser()
       parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati/yellow_tripdata_2020-'+'0'+str(i)+'.csv')
       args=parser.parse_args()
       df=df.append(pd.read_csv(args.input_data))
       i+=1
       
 except FileNotFoundError:
          print('Il file non esiste')
          i+=1



df1=pd.read_csv('taxi+_zone_lookup.csv')



# trasformo i NaN in 0 

replace_Nan_with_zeros(df)
       


# Creo nuova colonna con datatime trasformato in timestemp


# df.index=df['VendorID'];
# df2=pd.DataFrame(list((df['VendorID'])), columns=['Vendor ID'])

# vendors=df['VendorID'].unique();

# for vendor in vendors:
#   for i in range(len(df.loc[vendor,'tpep_pickup_datetime'])):
    
#     data=datetime.strptime(list(df.loc[vendor,'tpep_pickup_datetime'])[i], '%Y-%m-%d %H:%M:%S')
#     df2[vendor,'Inizio Corsa'][i]=(datetime.timestamp(data))

'''
Trasformo in timestamp le date di partenza delle corse. Imposto su tali date un anno, un mese e un giorno fissato così
da poterle poi confrontare con una data (anno-mese-giorno 00:00:00) di riferimento ed estrarre solo la distanza temporale in ore, minuti e secondi

'''

# usare apply

for i in range(1000):
    data=datetime.strptime(df['tpep_pickup_datetime'][i],'%Y-%m-%d %H:%M:%S')
    data=data.replace(day=1,month=1,year=2020)
    df.loc[i,'Inizio Corsa']=(datetime.timestamp(data))
   

#creato un unico dataframe che associa alla PULocationID il borough corrispondente

df1 = df1.rename({'LocationID': 'PULocationID'}, axis=1)
df_merged = pd.merge(df, df1, on=['PULocationID'],how='left')
    


#Individuo fasce orarie

fasce_orarie=np.array(range(0,25))*3600

#Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista


numero_passeggeri=count_passengers_hour(df,fasce_orarie)












