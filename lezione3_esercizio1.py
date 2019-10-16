# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 01:00:01 2019

@author: Danilo

Testo:  Scrivere una funzione che riceve tre numeri
        interi g, m, a (si ipotizza che a sia sempre un 
        numero dispari per evitare anni bisestili) e 
        restituisce True o False a seconda se i tre numeri
        formano una data valida nel formato "g/m/a". 
        Es: 30/2/2017 False, 1/1/1111 True.
"""

import datetime

def Data_Valida(g, m, a):
    
    risultato = True
    
    try:
        datetime.datetime(a, m, g)
    except ValueError:
        risultato = False
        
    
    return risultato


g = int(input("Inserisci il giorno: "))
m = int(input("Inserisci il mese: "))    
a = int(input("Inserisci l'anno: "))

print(Data_Valida(g, m, a))