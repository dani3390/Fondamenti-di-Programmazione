# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 00:23:17 2019

@author: Danilo

Testo: Scrivere una funzione 'invest' nel file 'invest.py',
che prende in input un capitale, un interesse annuale e un 
numero di anni e ritorna come intero il capitale maturato 
dopo un investimento di n anni all'interesse i. 
Usare la formula maturato = capitale * (1+interesse/100)**anni.

"""

def invest(capitale, interesse, anni):
    totale = int((capitale * (1 + interesse / 100) ** anni))
    
    return totale

from lezione2_esercizio5 import invest

test_list = {(1000,10,2):1210,
             (5000,1.10,20):6222,
             (3500,0.9,30):4579}

if __name__ == '__main__':
    for test_case, result in test_list.items():
        val = invest(*test_case)
        if  val == result:
            print('Test case: {}\tOK'.format(test_case))
        else:
            print('Test case: {}\tNOK, risultato atteso {}, risultato fornito {}'.format(test_case, result, val))

