#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:49:30 2020

@author: francescaronci
"""
from datetime import datetime

def count_passengers_hour(DataFrame,fasce_orarie):
#imposto una data di riferimento

 ora_riferimento=datetime.timestamp(datetime.strptime('2020-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

#Calcolo il numero di passeggeri per fascia oraria e li salvo in una lista

 numero_passeggeri=[]
 for j in range(len(fasce_orarie)-1):
    passeggeri=0
    for i in range(1000):
        
#tutte le corse che cadono dalle 00:00 alle 01:00
       if fasce_orarie[j]<(abs((DataFrame['Inizio Corsa'][i]-ora_riferimento)))<fasce_orarie[j+1]:
            
           passeggero=int((DataFrame['passenger_count'][i]))
           passeggeri+= passeggero
    numero_passeggeri.append(passeggeri)
 return numero_passeggeri