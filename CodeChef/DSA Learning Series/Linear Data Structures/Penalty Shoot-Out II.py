t = int(input())
for _ in range(t):
    n = int(input())
    l = list(input())
    ans = 0
    a,b = 0,0
    ia,ib = n,n
    for i in range(0,2*n):
        if i%2 == 0:
            a += int(l[i])
            ia -= 1
        else:
            b += int(l[i])
            ib -= 1
        ans += 1
        if a > (b+ib):
            break
        elif b > (a+ia):
            break
            
    print(ans)
