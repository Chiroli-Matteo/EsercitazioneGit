# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
somma = 0 

while True :
    numero = int(input("inserisci numero intero, se vuoi terminare l'attività inserisci 0: "))
    
    if numero == 0 :
        break
    
    somma += numero 
    
print("la somma dei numeri inseriti è: ", somma)