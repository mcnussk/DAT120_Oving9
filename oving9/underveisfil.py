# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 10:35:45 2021

@author: Magnu
"""
# splitte ved :, ta tallverdi inn som svar, splitte ved :, 
#append hver verdi inn i en liste som spørsmål

"""sporsmaal = []
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
    teller = teller + 1"""
    l = [i.strip('[]') for i in l]
    
  hello = [x.strip(' ') for x in hello]

"""testis = " 2 "
if testis == input("kjørdåå"):
    print("ez")
else:
    print(":(")
    
    for alt in fil_alternativer[teller]:
                alt_teller = 0
                print(str(alt_teller) + ": " + fil_alternativer[teller])
                alt_teller += 1"""
    
""" s1 = "Hvor høyt er Eiffeltårnet?"
    s1list = ["(1) 324 meter", "(2) 354 meter", "(3) 374 meter"]
    s1riktig = 1
    
    s2 = "Hvor mange bein har en sommerfugl?"
    s2list = ["(1) 4", "(2) 8", "(3) 6"]
    s2riktig = 3
    
    spill = Flervalg(s1, s1list, s1riktig)
    spill2 =Flervalg(s2, s2list, s2riktig)
    print(spill)
    spill.sjekk_svar()
    print(spill2)
    spill2.sjekk_svar()"""
    