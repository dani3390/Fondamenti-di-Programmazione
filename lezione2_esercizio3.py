# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:11:03 2019

@author: Danilo

Testo:  Scrivere una funzione che dati in ingresso il numero
        dei maschi e delle femmine che entrano in discoteca, la 
        funzione calcola e stampa a video il prezzo totale sapendo 
        che i primi pagano 12€ e le seconde 10€
"""

def Femminismo(maschi, femmmine):
    costo = (maschi * 12) + (femmine * 10)
    
    return costo

maschi = int(input("Inserisci il numero di maschi: "))

femmine = int(input("Inserisci il numero di femmine: "))

print(Femminismo(maschi, femmine))