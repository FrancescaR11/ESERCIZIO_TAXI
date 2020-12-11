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

parser=argparse.ArgumentParser()

parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati/yellow_tripdata_2020-02.csv')
<<<<<<< HEAD

parser.add_argument("-i2", "--input_data2", help="Complete path to the file containing taxi+_zone_lookup",
                    type=str, default='./dati/taxi+_zone_lookup.csv')
=======
>>>>>>> 98b5e9c06ec50e57019afa699c0fc1eb045a069b

args=parser.parse_args()

# salvo i dati su una struttura di tipo DataFrame 

df= pd.read_csv(args.input_data)
df1=pd.read_csv(args.input_data2)
# Altro meteodo
# df= pd.read_csv('./yellow_tripdata_2020.csv', nrows=5)

# mettere nel file git ignore la cartella dove si trovano i dati

# trasformo i NaN in 0 

df['VendorID'].fillna(0, inplace=True)

df['passenger_count'].fillna(0, inplace=True)

df['RatecodeID'].fillna(0, inplace=True)

df['store_and_fwd_flag'].fillna(0, inplace=True)

df['payment_type'].fillna(0, inplace=True)

# Creo nuova colonna con datatime trasformato in timestemp


# df.index=df['VendorID'];
# df2=pd.DataFrame(list((df['VendorID'])), columns=['Vendor ID'])

# vendors=df['VendorID'].unique();

# for vendor in vendors:
#   for i in range(len(df.loc[vendor,'tpep_pickup_datetime'])):
    
#     data=datetime.strptime(list(df.loc[vendor,'tpep_pickup_datetime'])[i], '%Y-%m-%d %H:%M:%S')
#     df2[vendor,'Inizio Corsa'][i]=(datetime.timestamp(data))

for i in range(1000):
    data=datetime.strptime(df['tpep_pickup_datetime'][i],'%Y-%m-%d %H:%M:%S')
    data=data.replace(day=1,month=2)
    df.loc[i,'Inizio Corsa']=(datetime.timestamp(data))

#creato un unico dataframe
df1 = df1.rename({'LocationID': 'PULocationID'}, axis=1)
df_merged = pd.merge(df, df1, on=['PULocationID'])
    
#Individuo fasce orarie
#se sottraggo due date mi restituisce la distanza in secondi

ora_riferimento=datetime.timestamp(datetime.strptime('2020-02-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
fasce_orarie=np.array(range(0,25))*3600
numero_passeggeri=[]
for j in range(len(fasce_orarie)-1):
    passeggeri=0
    for i in range(1000):
        
        #tutte le corse che cadono dalle 00:00 alle 01:00
        if fasce_orarie[j]<(abs(df['Inizio Corsa'][i]-ora_riferimento))<fasce_orarie[j+1]:
            
             passeggero=int(df['passenger_count'][i])
             passeggeri+=passeggero
    numero_passeggeri.append(passeggeri)












