#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Scrivere una funzione che prende come argomento una stringa contenente una serie di parole (sequenze di caratteri separate da spazi bianchi, tabulazioni o a capo) e un intero e ritorna il numero di parole presenti nella stringa che hanno una lunghezza esattamente pari all'intero preso come argomento
"""

def conta_parole(stringa, lunghezza):
#    scrivere qui il codice
    lista = stringa.split()
    numero = 0
    
    for elemento in lista:
        if (len(elemento) == lunghezza):
            numero = numero + 1
    
    return numero