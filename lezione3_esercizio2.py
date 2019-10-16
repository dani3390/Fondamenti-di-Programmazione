# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:02:49 2019

@author: Danilo

Testo:  Scrivere una funzione che prende una
        lista di interi e restituisce la somma di 
        tutti i numeri pari meno la somma di tutti
        i numeri dispari che la compongono.
"""

def Pari_Meno_Dispari(lista):
    somma_pari = 0
    somma_dispari = 0
    
    for elemento in lista:
        if ((elemento % 2) == 0):
            somma_pari = somma_pari + elemento
        else:
            somma_dispari = somma_dispari + elemento
    
    totale = somma_pari - somma_dispari
    
    return totale


lista = [7, 12, 9, 5 , 94, 6, 19, 57, 8, 100, 77]

print(Pari_Meno_Dispari(lista))

