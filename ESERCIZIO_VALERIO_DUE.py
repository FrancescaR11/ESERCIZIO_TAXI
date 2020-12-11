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

parser=argparse.ArgumentParser()

parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati/yellow_tripdata_2020-02.csv')

args=parser.parse_args()

# salvo i dati su una struttura di tipo DataFrame 

df= pd.read_csv(args.input_data)

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

for i in range(400000):
    data=datetime.strptime(df['tpep_pickup_datetime'][i],'%Y-%m-%d %H:%M:%S')
    data.replace(day=1)
    df.loc[i,'Inizio Corsa']=datetime.timestamp(data)

# ora_interesse=  ('00:00:00')
# ora_interesse=datetime.strptime(ora_interesse,'%H:%M:%S')

# ora=datetime.timestamp(ora_interesse)












