# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 23:56:48 2019

@author: Danilo

Testo:  Scrivere una funzione che dati in ingresso 
        il costo del biglietto per visitare un museo e il 
        numero di studenti di una classe in gita scolastica, 
        ritorna la spesa totale, considerando che se gli studenti
        sono compresi fra 10 e 30 il biglietto per studente costa
        il 20% in meno, se sono 31 o più il 30% in meno.
"""

def Sconto_Scuola_Museo(biglietto, numero):   #Si può anche fare lo sconto direttamente sul totale
    if (numero > 0 and numero < 10):
        costo = biglietto * numero
    elif (numero >= 10 and numero <= 30):
        sconto = round(((biglietto * 20) / 100), 2)
        costo = (biglietto - sconto) * numero
    elif (numero >= 31):
        sconto = round(((biglietto * 30) / 100), 2)
        costo = (biglietto - sconto) * numero
    else: 
        print("Hai inserito un valore negativo") #possibile errore non gestito
    
    return costo


biglietto = float(input("Inserisci il costo del biglietto: "))

numero = int(input("Inserisci il numero degli studenti: "))

print(Sconto_Scuola_Museo(biglietto, numero))
