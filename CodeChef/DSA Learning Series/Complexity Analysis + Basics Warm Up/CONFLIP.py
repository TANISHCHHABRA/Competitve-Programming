# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:30:41 2020

@author: TANIS
"""

g = int(input())
for i in range(g):
    t = int(input())
    for j in range(t):
        count = 0
        a = input().split(" ")
        initial_state = int(a[0])
        no_of_round = int(a[1])
        final_state = int(a[2])
        if(no_of_round % 2 == 0):
            print(no_of_round//2)           
        else:
            if(initial_state == final_state):
                print((no_of_round-1)//2)
            else:
                print((no_of_round+1)//2)
