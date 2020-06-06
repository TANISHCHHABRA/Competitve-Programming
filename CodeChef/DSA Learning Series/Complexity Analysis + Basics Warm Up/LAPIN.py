t = int(input())
for i in range(t):
    s = input()
    l = int(len(s)/2)
    if(len(s)%2 == 0):
        s_left = list(s[:l])
        s_right = list(s[l:])
    else:
        s_left = list(s[:l])
        s_right = list(s[l+1:])
        
    flag = 0
    for i in s_left:
        if i in s_right:
            s_right.remove(i)
        else:
            print("NO")
            flag = 1
            break
    if(flag == 0):
        print("YES")
