x = input().split()
a = input().split()
b = input().split()
for i in range(int(x[0])):
    a[i] = [int(a[i]),i]
for i in range(int(x[1])):
    b[i] = [int(b[i]),i]
    
a.sort()
b.sort()
for i in range(int(x[1])):
    print(a[0][1],b[i][1])
for i in range(1,int(x[0])):
    print(a[i][1],b[int(x[1])-1][1])
