# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:31:01 2021

@author: Magnu
"""

#Klasse flervalg
class Flervalg:
    def __init__( self, spmtekst, alternativer, svar):
        self.spmtekst = spmtekst
        self.svar = svar
        self.alternativer = alternativer

#spmtekst, liste med alternativer, tall som representerer rett svar

#metode __str__
    def __str__(self):
        sporsmaal = ""
        sporsmaal += self.spmtekst + '\n'
        sporsmaal += "alternativer: \n"
        for alternativ in self.alternativer:
            sporsmaal += alternativ +"\n"
        return sporsmaal
        
        
#metode sjekk svar, tar imot heltall som representerer svar
    def sjekk_svar(self):
        brukersvar = int(input("Skriv inn svaret som et heltall 1-3: "))
        if brukersvar == self.svar:
            print("\nRiktig svar!\n")
        else:
            print("\nDet var visst feil.")
            print("Det riktige svaret var alternativ " + str(self.svar) + "\n")
        
#metode korrekt svar tekst, skal returnere teksten for riktig svar
    def korrekt_svar_tekst(self):
         return self.svar
         
         
if __name__ == "__main__":
    s1 = "Hvor høyt er Eiffeltårnet?"
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
    spill2.sjekk_svar()
    
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
    
    
    
