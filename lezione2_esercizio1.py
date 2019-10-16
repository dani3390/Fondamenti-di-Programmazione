# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:47:35 2019

@author: Danilo

Testo:  Scrivere una funzione che dati in ingresso il prezzo
        di un prodotto e il valore percentuale dello sconto, la 
        funzione calcola e stampa a video il prezzo finale
"""

def Prezzo_Finale(prezzo, percentuale):
    sconto = round(((prezzo * percentuale) / 100), 2)
    prezzo = prezzo - sconto
    return prezzo

prezzo = float(input("Inserisci il prezzo del prodotto: "))

percentuale = int(input("Inserisci la percentuale di sconto: "))

print(Prezzo_Finale(prezzo, percentuale))


