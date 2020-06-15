"""
def solve(ts):
    ans = 0
    js_even = 0
    if ts%2!=0:
        ans = ts//2
    else:
        js_even = ts//2
        js_odd = ts//2
        ts = ts//2
        while True:
            if ts%2 != 0:
                js_even = js_even//2
                js_odd = js_odd//2 + 1
                ans = js_even
                break
            if js_even%2 != 0:
                break
            js_even = js_even//2
            ts = ts//2
    return ans
"""
def native(ts):
    if ts % 2 == 0:
        while(ts % 2 == 0):
            ts = ts // 2
        j = (ts - 1) // 2
    else:
        j = (ts - 1) // 2
    return j
    


t = int(input())
for i in range(t):
    a= int(input())
    print(native(a))
