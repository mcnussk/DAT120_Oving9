# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:35:45 2021

@author: Magnu
"""
# splitte ved :, ta tallverdi inn som svar, splitte ved :, 
#append hver verdi inn i en liste som spørsmål

sporsmaal = []
fil_sporsmaal = []
fil_korrekt_svar = []
fil_alternativer = []
teller = 0
tekstfil = open("sporsmaalsfil.txt", "r", encoding = "UTF8")
for linje in tekstfil:
    rad = linje.split(":")
    fil_sporsmaal.append(rad[0])
    fil_korrekt_svar.append(rad[1])
    fil_alternativer.append(rad[2])
    print(fil_sporsmaal[teller])
    print(fil_korrekt_svar[teller])
    print(fil_alternativer[teller])
    teller = teller + 1
    

    