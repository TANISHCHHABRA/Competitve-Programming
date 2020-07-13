# Enter your code here. Read input from STDIN. Print output to STDOUT# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 15:35:52 2020

@author: TANIS
"""

a = list(input().split(" "))
n = int(a[0])
m = int(a[1])

i = 1
j = 1
x = 1
while i <= n//2:
    t = j*x
    temp = (m - (t*3))//2
    print('-'*temp+'.|.'*t+'-'*temp)
    x += 2
    i += 1
    
temp = (m-7)//2
print('-'*temp+"WELCOME"+'-'*temp)

i = 1
j = 1
x = (m - 6)//3
while i <= n//2:
    t = j * x
    temp = (m - (3*t))//2
    print('-'*temp+'.|.'*t+'-'*temp)
    x -= 2
    i += 1
