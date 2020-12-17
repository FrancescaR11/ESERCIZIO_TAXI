#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 17:35:23 2020

@author: francescaronci
"""

def replace_Nan_with_zeros(DataFrame):
 
    nomi_colonne=list(DataFrame.columns)

    for nome in nomi_colonne:
     if DataFrame[nome].isnull().sum().sum() > 0:
        DataFrame[nome].fillna(0, inplace=True)   