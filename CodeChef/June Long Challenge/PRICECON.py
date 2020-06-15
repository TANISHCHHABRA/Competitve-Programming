t = int(input())

for i in range(t):
    a = list(input().split(" "))
    k = int(a[1])
    b = list(input().split(" "))
    ans = 0
    for i in b:
        if int(i) > k:
            ans = ans + (int(i)-k)
    print(ans)
