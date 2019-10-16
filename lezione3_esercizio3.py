# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 09:08:17 2019

@author: Danilo

Testo:  Scrivere una funzione che prende in
        input una stringa di parole separate da 
        spazi e restituisce una lista con le 
        lunghezze delle parole della stringa.
"""

def Lunghezza_Parole(stringa):
    lista = []
    
    for elemento in stringa.split():
        lista.append(len(elemento))
        
        
    print(lista)
    
    
stringa = "lella lolla lulla caca rara"

Lunghezza_Parole(stringa)
        
        


