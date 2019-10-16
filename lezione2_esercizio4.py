# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:13:29 2019

@author: Danilo

Testo:  Scrivere una funzione che prende in input
        due interi e una stringa. In base al contenuto della 
        stringa, che conterrà una operazione, la funzione 
        eseguirà le 4 operazioni di base con i due interi: 
        addizione, sottrazione, moltiplicazione, divisione.
"""

def Operazioni_Aritmetiche(stringa, numero1, numero2):
    if (stringa == "addizione"):
        risultato = numero1 + numero2
    elif (stringa == "sottrazione"):
        risultato = numero1 - numero2
    elif (stringa == "moltiplicazione"):
        risultato = numero1 * numero2
    elif (stringa == "divisione"):
        risultato = numero1 / numero2
    else:
        print("Errore") #non gestito
        
    return risultato

stringa = input("Inserisci una delle quattro operazioni base: ")

numero1 = int(input("Inserisci il primo numero: "))

numero2 = int(input("Inserisci il secondo numero: "))

print(Operazioni_Aritmetiche(stringa, numero1, numero2))