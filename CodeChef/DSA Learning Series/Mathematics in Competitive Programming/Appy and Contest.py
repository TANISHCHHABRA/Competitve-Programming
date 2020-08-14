def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcm(a,b):
    return (a*b)/gcd(a,b)

t = int(input())

for _ in range(t):
    s = input().split()
    n = int(s[0])
    a = int(s[1])
    b = int(s[2])
    k = int(s[3])
    
    ans = n//a + n//b - 2*(n//lcm(a,b))
        
    if ans >= k:
        print("Win")
    else:
        print("Lose")
