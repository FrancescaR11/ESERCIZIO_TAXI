# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:21:08 2020

@author: gaiad
"""

import pandas as pd
import argparse
from datetime import datetime
import time
import numpy as np
from abc import ABC, abstractmethod
from os.path import splitext
from Eliminazione_Nan import replace_Nan_with_zeros
from Conteggio_passeggeri import count_passengers_hour
from Conversione_timestamp import to_timestamp
import matplotlib.pyplot as plt
from Conteggio_passeggeri import count_max_passengers

i=1
while i in range(13):
  try:
    
      parser=argparse.ArgumentParser()
      parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati/yellow_tripdata_2020-'+'0'+str(i)+'.csv')
      args=parser.parse_args()
      i+=1
      
  except FileNotFoundError:
          print('Il file non esiste')
          i+=1



class TaxiReader(ABC):
    """
    interface
    """

    @abstractmethod
    def get_list_of_taxi(self):
        """
        abstract method
        """
        pass

    @staticmethod
    def create_instance(filename):
        suffix = splitext(filename)[1][1:].lower()
        if suffix == 'json':
            return JSONReader(filename)
        elif suffix == 'csv':
            return CSVReader(filename)
        else:
            raise ValueError('unknown file type')
            
class JSONReader(TaxiReader):

    def __init__(self, filename):
        self.filename = filename

    def get_list_of_taxi(self):
        raise ValueError('JSON Reader not yet implemented')
        
        
class CSVReader(TaxiReader):

    def __init__(self, filename):
        self.filename = filename
        
        
    def get_list_of_taxi(self):
        
               

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

        return df
     
class CleanData:
    
    def __init__(self):
        pass
        
    def prepare_data(self, df):
        '''
        pulizia NaN
        conversione timestamp
        df merged
        
        '''
        replace_Nan_with_zeros(df)
        
        df['Inizio Corsa']=df['tpep_pickup_datetime'].apply(to_timestamp) 
        
        #Importo il file dei boroughs
        df1=pd.read_csv('taxi+_zone_lookup.csv')
        df1 = df1.rename({'LocationID': 'PULocationID'}, axis=1)
        df_merged = pd.merge(df, df1, on=['PULocationID'],how='left')
        
        return df_merged
        return df
        
class CountPassengers:

    def __init__(self):
        pass

    def passengers_counter(self, df_merged):
        
        #Estraggo il numero di borough
        boroughs=list(df_merged['Borough'].unique())

        
        #Individuo fasce orarie
        fasce_orarie=np.array(range(0,25))*3600
                
        
        #Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista
        df_passeggeri=count_passengers_hour(df_merged,boroughs,fasce_orarie)

        return df_passeggeri, boroughs
        

class PlotFeatures:
            
    def __init__(self):
        pass 
        
    def features_plotter(self, df, boroughs, df_passeggeri):
    
        colori= ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        plt.figure(figsize=(24,20))    
        
        for k in range(len(boroughs)):
            plt.subplot(4,2,k+1)
            df_passeggeri[boroughs[k]].plot(kind='bar', title=boroughs[k],color=colori[k])
            plt.grid(True)
            plt.ylabel('Numero passeggeri')
            plt.xlabel('Fasce orarie')
            plt.ylim(0, count_max_passengers(boroughs,df_passeggeri))
        
        
        figura=plt.savefig('Grafico.png')
        return figura
    
    
reader = TaxiReader.create_instance(args.input_data)
df = reader.get_list_of_taxi()

cleaner = CleanData()
df_merged = cleaner.prepare_data(df)

counter=CountPassengers()
df_passeggeri=counter.passengers_counter(df_merged)

counter=CountPassengers()
df_passeggeri,boroughs=counter.passengers_counter(df_merged)

plotter=PlotFeatures()
figura=plotter.features_plotter(df, boroughs, df_passeggeri)