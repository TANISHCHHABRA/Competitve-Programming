class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num<=0:
            return False
        num = bin(num)[2:]
        o = 0
        for i in num:
            if i == '1':
                o += 1
        if o != 1:
            return False
        o = False
        z = 0
        for i in num:
            if o:
                z += 1
            if i == '1':
                o = True
        if z%2 == 0:
            return True
        return False
        
