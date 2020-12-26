# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:08:59 2020

@author: gaiad
"""

from datetime import datetime

'''

Trasformo in timestemp le date di partenza delle corse. Imposto su tali date un anno, un mese e un giorno fissato (2020-01-01),
così da poterle poi confrontare con una data di riferimento ed un orario (2020-01-01 00:00:00) ed etrarre solo la distanza
temporale in ore, minuti e secondi.
La funzione restituisce le nuove date in formato timestamp.

'''

def to_timestamp(x):
       
        date=datetime.strptime(x, '%Y-%m-%d %H:%M:%S') # Converto le date in formato datetime
        date=date.replace(day=1,month=1,year=2020) # Sostituisco il giorno, il mese e l'anno per il confronto con la data e l'orario di riferimento
        date=datetime.timestamp(date) #  Converto le date in formato timestamp
        
        return date
    
