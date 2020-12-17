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


         

<<<<<<< HEAD
# salvo i dati su una struttura di tipo DataFrame 

=======
parser=argparse.ArgumentParser()

parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati')


# parser.add_argument("-i2", "--input_data2", help="Complete path to the file containing taxi+_zone_lookup",
#                     type=str, default='./dati/taxi+_zone_lookup.csv')
df1=pd.read_csv('taxi+_zone_lookup.csv')
>>>>>>> 7f17606aa271328235748fa1b96aa6952de1ffe0

df1=pd.read_csv('taxi+_zone_lookup.csv')


<<<<<<< HEAD
=======
df= pd.read_csv(args.input_data)
#df1=pd.read_csv(args.input_data2)
# Altro meteodo
# df= pd.read_csv('./yellow_tripdata_2020.csv', nrows=5)
>>>>>>> 7f17606aa271328235748fa1b96aa6952de1ffe0

# trasformo i NaN in 0 (farlo con un if)

# fare for per lista delle colonne

df['VendorID'].fillna(0, inplace=True)

df['passenger_count'].fillna(0, inplace=True)

df['RatecodeID'].fillna(0, inplace=True)

df['store_and_fwd_flag'].fillna(0, inplace=True)

df['payment_type'].fillna(0, inplace=True)
#mettere un if sui nan

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
<<<<<<< HEAD
'''

# usare apply

=======

'''
>>>>>>> 7f17606aa271328235748fa1b96aa6952de1ffe0
for i in range(1000):
    data=datetime.strptime(df['tpep_pickup_datetime'][i],'%Y-%m-%d %H:%M:%S')
    data=data.replace(day=1,month=2,year=2020)
    df.loc[i,'Inizio Corsa']=(datetime.timestamp(data))
    #trasforma in apply

#creato un unico dataframe che associa alla PULocationID il borough corrispondente
df1 = df1.rename({'LocationID': 'PULocationID'}, axis=1)
<<<<<<< HEAD
df_merged = pd.merge(df, df1, on=['PULocationID'], how= 'left')
    
=======
df_merged = pd.merge(df, df1, on=['PULocationID'],how='left')
    


>>>>>>> 7f17606aa271328235748fa1b96aa6952de1ffe0
#imposto una data di riferimento
ora_riferimento=datetime.timestamp(datetime.strptime('2020-02-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

#Individuo fasce orarie
fasce_orarie=np.array(range(0,25))*3600

#Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista
<<<<<<< HEAD

=======
>>>>>>> 7f17606aa271328235748fa1b96aa6952de1ffe0
numero_passeggeri=[]
for j in range(len(fasce_orarie)-1):
    passeggeri=0
    for i in range(1000):
        
        #tutte le corse che cadono dalle 00:00 alle 01:00
        if fasce_orarie[j]<(abs(df['Inizio Corsa'][i]-ora_riferimento))<fasce_orarie[j+1]:
            
             passeggero=int(df['passenger_count'][i])
             passeggeri+=passeggero
    numero_passeggeri.append(passeggeri)












