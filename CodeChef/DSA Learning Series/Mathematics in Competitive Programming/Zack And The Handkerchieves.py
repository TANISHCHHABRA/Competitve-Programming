def gcd(x,y):
    while y:
        x,y = y, x%y
    return x
    
for _ in range(int(input())):
    a = input().split()
    l = int(a[0])
    b = int(a[1])
    ans = int(gcd(l,b))
    if ans > 1:
        print(ans)
    else:
        print(1)
