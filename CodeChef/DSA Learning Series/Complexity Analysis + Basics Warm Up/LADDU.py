# -*- coding: utf-8 -*-
"""
Created on Thu May 21 18:30:41 2020

@author: TANIS
"""

t = int(input())
for i in range(t):
    a = input()
    a = a.split(" ")
    a_activities = int(a[0])
    a_origin = a[1]
    l = []
    for n in range(a_activities):
        a = input()
        l.append(a)
    laddus = 0
    for i in l:
        i = i.split(" ")
        if i[0] == "CONTEST_WON":
            laddus += 300
            if(int(i[1]) <= 20):
                laddus += (20 - int(i[1]))
        elif i[0] == "TOP_CONTRIBUTOR":
            laddus += 300
        elif i[0] == "BUG_FOUND":
            laddus += int(i[1])
        elif i[0] == "CONTEST_HOSTED":
            laddus += 50
    ans = 0
    if(a_origin == "INDIAN"):
        ans = laddus//200    
    else:
        ans = laddus//400
    print(ans)
