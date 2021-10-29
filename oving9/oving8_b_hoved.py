# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 12:09:04 2021

@author: Magnu
"""

from oving8_b import Flervalg

sporsmaaltekst = [
    "A er riktig svar. \n(1) apekatt \n(2) løve \n(3) pickle \n", 
    "Hvem er din favorittgymlærer? \n(1) toogood \n(2) OGS \n(3) dvdd \n"
]

sporsmaal = [
    Flervalg(sporsmaaltekst[0], "1"),
    Flervalg(sporsmaaltekst[1], "2")
]

def run_test(sporsmaal):
    poeng = 0
    for spm in sporsmaal:
        svar = input(spm.spmtekst)
        if svar == spm.svar:
            poeng +=1
    print("Du svarte " + str(poeng) + "/" + str(len(sporsmaal)) + " riktig")
    
run_test(sporsmaal)



