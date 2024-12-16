# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:19:29 2024

@author: PMBARD
"""
def dico():
    import requests
    import random
    
    url = "http://109.10.114.61/300_mots_pendus.txt"
    response = requests.get(url)        
    liste = response.text.splitlines()
    mot = random.choice(liste)
