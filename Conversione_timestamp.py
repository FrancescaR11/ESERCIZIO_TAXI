# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 18:08:59 2020

@author: gaiad
"""

from datetime import datetime

def to_timestamp(x):
       
        date=datetime.strptime(x, '%Y-%m-%d %H:%M:%S')
        date=date.replace(day=1,month=2,year=2020)
        date=datetime.timestamp(date)
        
        return date
    
