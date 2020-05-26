class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        if(num == 1):
            return True
        l = 0
        h = num
        #while l <= h:
        for i in range(int(log2(num)) + 2):
            mid = int((l+h)/2)
            mid_sq = mid**2
            if(mid_sq == num):
                return True
            elif(mid_sq < num):
                l = mid
            elif(mid_sq > num):
                h = mid
        return False
