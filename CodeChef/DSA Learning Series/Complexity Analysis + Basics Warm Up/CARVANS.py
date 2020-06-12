t = int(input())
for j in range(t):
    n = int(input())
    s = input().split(" ")
    count = 1
    if n == 1:
        print(count)
    else:
        for i in range(1,n):
            if(s[i-1] >= s[i]):
                count += 1
            else:
                s[i] = s[i-1]
        print(count)     
