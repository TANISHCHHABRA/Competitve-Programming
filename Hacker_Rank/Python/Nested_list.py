d = {}
t = int(input())
for i in range(t):
    a = input()
    d[a] = float(input())
    
key_min = min(d.keys(), key = (lambda k: d[k]))

mini = d[key_min]
a = {}
for i in d:
    if d[i] != mini:
        a[i] = d[i]

key_min = min(a.keys(), key = (lambda k: a[k]))

mini = a[key_min]

l = []

for i in a:
    if a[i] == mini:
        l.append(i)
l.sort()
for i in l:
    print(i)
