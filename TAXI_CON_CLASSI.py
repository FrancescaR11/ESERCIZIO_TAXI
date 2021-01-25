# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 18:21:08 2020

@author: gaiad, francescaronci
"""

import pandas as pd
import argparse
import numpy as np
from abc import ABC, abstractmethod
from os.path import splitext
from Eliminazione_Nan import replace_Nan_with_zeros
from Conteggio_passeggeri import count_passengers_hour
from Conversione_timestamp import to_timestamp
import matplotlib.pyplot as plt
from Conteggio_passeggeri import count_max_passengers
import os
import time
from tqdm import tqdm


# Creo la classe astratta TaxiReader 

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
            

# Creo la classe che legge i dati in formato JSON            
            

class JSONReader(TaxiReader):

    def __init__(self, filename):
        self.filename = filename

    def get_list_of_taxi(self):
        raise ValueError('JSON Reader not yet implemented')
        
            
# Creo la classe che legge i dati in formato CSV 
        

class CSVReader(TaxiReader):

    def __init__(self, filename):
        
        self.filename = filename
        
        
    def get_list_of_taxi(self,df):
           
        df=df.append(pd.read_csv(self.filename , low_memory=False )) # appendo al DataFrame del mese i-1 quello dell' i-esimo mese

        return df # restituisco il DataFrame contente i dati di tutti i mesi fino a quello di indice i

'''

Creo classe che elimina i NaN, aggiunge a df una colonna contenete le date in formato timestemp, 
unisce i due DataFrame di Input e restituisce un unico DataFrame completo

'''
class CleanData:
    
    def __init__(self):
        pass
        
    def prepare_data(self, df):

        replace_Nan_with_zeros(df)
        
        tqdm.pandas(desc='Esecuzione conversione timestamp') #Descrizione funzione barra di avanzamento
        #Il metodo '.progress_apply()' viene utilizzato al posto del metodo tradizionale '.apply()' per visualizzare la barra di avanzamento
        df['Inizio Corsa']=df['tpep_pickup_datetime'].progress_apply(to_timestamp) 
        
        #Importo il seconod DataFrame di Input
        df1=pd.read_csv('./dati/taxi+_zone_lookup.csv')
        
        #Per eseguire il merge, assegno alla colonna di df1 lo stesso nome della colonna  di df
        df1 = df1.rename({'LocationID': 'PULocationID'}, axis=1)
        
        # Faccio il merge dei due DataFrame rispetto ai dati contenuti in df (non ci interessano zone non presenti in df)
        df_merged = pd.merge(df, df1, on=['PULocationID'],how='left')
        
        return df_merged



# Creo classe che conta il numero di passeggeri per fasce orarie per ogni borough        

class CountPassengers:

    def __init__(self):
        pass

    def passengers_counter(self, df_merged):
        
        #Estraggo il numero di boroughs
        boroughs=list(df_merged['Borough'].unique())

        
        #Individuo vettore contenete fasce orarie, da 0 a 24, espresse in secondi
        vettore_temporale=np.array(range(0,25))*3600
                
        
        #Calcolo il numero di passeggeri per fascia oraria 
        df_passeggeri=count_passengers_hour(df_merged,boroughs,vettore_temporale)

        return df_passeggeri, boroughs
        
'''

Creo classe che esegue il plot delle features calcolate. Per ogni borough costruisce un istogramma di colore diverso,
dove l'asse x rappresenta le fasce orarie, e l'asse y il numero di passeggeri.

'''
class PlotFeatures:
            
    def __init__(self):
        pass 
        
    def features_plotter(self, boroughs, df_passeggeri):
    
        colori= ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        plt.figure(figsize=(24,20))    
        
        for k in range(len(boroughs)):
            
            plt.subplot(4,2,k+1)
            
            df_passeggeri[boroughs[k]].plot(kind='bar', title=boroughs[k],color=colori[k])
            
            plt.grid(True)
            
            plt.ylabel('Numero passeggeri')
            
            plt.xlabel('Fasce orarie')

            '''
            
           Volendo ottenere una rappresntazione in scala, questa linea di codice, chiamando la funzione "count_max_passengers",
           imposta come limite dell'asse y il massimo numero di passeggeri ottenuto tra tutti i boroughs e tra tutte le fasce orarie
           
            ''' 
            #plt.ylim(0, count_max_passengers(boroughs,df_passeggeri))
                
        figura=plt.savefig('./results/Grafico.png') # Salvo la figura contenente tutti i subplot
        
        return figura


'''
        
Uso argparse e os per la lettura dei file.
Per ogni file contenuto nella cartella specificata dall'utente creo l'oggetto reader che,
tramite il metodo get_list_of_taxi(), appende al DataFrame "df" i dati contenuti in ciasucn file.

         
'''

start = time.perf_counter() #  Avvio conteggio del tempo di esecuzione

df=pd.DataFrame()
    

parser=argparse.ArgumentParser()

parser.add_argument("-i", "--input_data", help="Complete path to the file containing yellow_tripdata",
                    type=str, default='./dati_ridotti/')

args=parser.parse_args()

dirs = os.listdir( args.input_data) # Creo lista dei file contenuti nella cartella specificata dal parser

for file in dirs: # Leggo i file relativi ai dati di input contenuti nella cartella
     
    if (file != ('taxi+_zone_lookup.csv')) & (file != ('.DS_Store')) :
      
         reader = TaxiReader.create_instance(args.input_data+file)    
       
         df = reader.get_list_of_taxi(df)

    

cleaner = CleanData()
df_merged = cleaner.prepare_data(df)


counter=CountPassengers()
df_passeggeri,boroughs=counter.passengers_counter(df_merged)

plotter=PlotFeatures()
figura=plotter.features_plotter(boroughs, df_passeggeri)

elapsed= time.perf_counter() - start # Calcolo il tempo impiegato per l'esecuzione

print ('Il tempo di esecuzione è' + ' ' +str(elapsed)) # Stampo il tempo impiegato per l'esecuzione


