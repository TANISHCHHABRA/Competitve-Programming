t = int(input())

for i in range(t):
    a = input()
    sum = 0
    j = 0
    while j < (len(a)-1):
        if a[j] == 'x':
            if a[j+1] == 'y':
                sum += 1
                j = j + 2
            else:
                j += 1
        else:
            if a[j+1] == 'x':
                sum += 1
                j = j + 2
            else:
                j += 1
    print(sum)
