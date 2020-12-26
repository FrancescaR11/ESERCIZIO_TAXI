# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 15:11:07 2020

@author: gaiad
"""

import argparse 
import pandas as pd

df=pd.DataFrame()

  
parser=argparse.ArgumentParser()
parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
             type=str, default='./dati/yellow_tripdata_2020-02.csv')
args=parser.parse_args()
df=df.append(pd.read_csv(args.input_data))

    
  
df=df.tail(200000)
df.to_csv('./dati_ridotti/yellow_tripdata_2020-02.csv')
