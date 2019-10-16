# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:38:01 2019

@author: Danilo

Testo:  Scrivere una funzione che prende in
        input una lista di interi e ritorna la lista
        con i complementi a 100 degli interi della lista in input.

"""


def Complemento_100(lista):
    
    lista_complementi = []
    
    for elemento in lista:
        lista_complementi.append(((10 ** len(str(elemento))) - elemento))  #basta modificare 10 con il complemento che si vuole fare
        
    print(lista_complementi)
    
    
lista = [765, 3174, 837, 483, 9492, 8482, 34, 2]    
    
Complemento_100(lista)
        

