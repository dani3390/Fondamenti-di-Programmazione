# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:32:58 2019

@author: Danilo

Testo:  Scrivere una funzione che verifica
        se una lista è ordinata in modo crescente 
        (<=) (supponiamo che la lista contenga oggetti ordinabili).
"""

def Ordinata_Crescente(lista):
    if sorted(lista) == lista:
        print("La lista è ordinata in modo crescente") 
        

lista = [12, 7, 84, 9, 15, 95, 0, 56]

Ordinata_Crescente(lista)