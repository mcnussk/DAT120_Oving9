# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:14:04 2021

@author: Magnu
"""

ordliste = dict()
linjeteller = 0
with open("oving_1_rein_tekst.txt", "r", encoding="UTF8") as fila:
    for linje in fila:
        ordene = linje.split()
        linjeteller += 1
        for ordet in ordene:
            ordet = ordet.strip(".")
            ordet = ordet.strip(",")
            ordet = ordet.lower()
            if ordet in ordliste:
                continue
            else:
                ordliste[ordet] = linjeteller
    for ordet in ordliste:
        print(f"Ordet {ordet} forekommer på linje nr {ordliste[ordet]} ")
        
        