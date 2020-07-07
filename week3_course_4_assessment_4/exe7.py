# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:03:37 2020

@author: mcsbi
"""
"""
The buggy code below prints out the value of the sport in the list sport. Use try/except so that the code will run properly. If the sport is not in the dictionary, ppl_play, add it in with the value of 1.
"""

sport = ["hockey", "basketball", "soccer", "tennis", "football", "baseball"]

ppl_play = {"hockey":4, "soccer": 10, "football": 15, "tennis": 8}

for x in sport:
    try:
        if x not in ppl_play.keys():
            ppl_play[x] = 1
    except Exception:
        pass

print(ppl_play)
