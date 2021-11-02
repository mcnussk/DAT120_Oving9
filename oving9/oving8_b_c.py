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
        teller = 0
        sporsmaal = ""
        sporsmaal += self.spmtekst + '\n'
        sporsmaal += "alternativer: \n"
        for alternativ in self.alternativer:
            sporsmaal +=  str(teller) + ": " + alternativ +"\n" 
            teller += 1
        return sporsmaal
        
        
#metode sjekk svar, tar imot heltall som representerer svar
    def sjekk_svar(self):
        brukersvar = input("Skriv inn svaret som et heltall 0-3: ")
        if brukersvar == self.svar:
            teller = 1
            return teller
        else:
            teller = 0
        return teller
  
#metode korrekt svar tekst, skal returnere teksten for riktig svar
    def korrekt_svar_tekst(self):
         print("Korrekt svar: " + self.alternativer[int(self.svar)] + "\n")
         
if __name__ == "__main__":
   
    
   
   def linjeleser():
        tekstfil = open("sporsmaalsfil.txt", "r", encoding = "UTF8")
        fil_sporsmaal = []
        fil_korrekt_svar = []
        fil_alternativer = []
        liste_spm = []
        for linje in tekstfil:
            linje = linje.strip()
            rad = linje.split(":")
            fil_sporsmaal.append(rad[0])
            fil_korrekt_svar.append(rad[1])
            fil_alternativer.append(rad[2].split(","))

            rad[2] = rad[2].strip().strip("[]")
            rad[2] = rad[2].strip(",")

            alt_liste = rad[2].split(",")
            alt_liste = [x.strip (" ") for x in alt_liste]  #fjerner mellomrommet før alternativene  
            liste_spm.append(Flervalg(rad[0], alt_liste, rad[1].strip()))
        return liste_spm
            
   sporsmol = linjeleser()
   
   poengsum1 = 0
   poengsum2 = 0
   for element in sporsmol:
       print(str(element))
       print("Spiller 1 sin tur!")
       value = element.sjekk_svar()
       if value == 1:
           korrekt1 = True
       else:
           korrekt1 = False
       poengsum1 += value
       print("Spiller 2 sin tur!")
       value = element.sjekk_svar()
       if value == 1:
           korrekt2 = True
       elif value == 0:
           korrekt2 = False
       poengsum2 += value
       
       
       element.korrekt_svar_tekst()
       if korrekt1 == True:
           print("Spiller 1: Korrekt")
       elif korrekt1 == False:
           print("Spiller 1: Feil")
       if korrekt2 == True:
           print("Spiller 2: Korrekt")
       elif korrekt2 == False:
           print("Spiller 2: Feil")
   print("\nSpiller 1 sin poengsum er " + str(poengsum1))
   print("Spiller 2 sin poengsum er " + str(poengsum2))