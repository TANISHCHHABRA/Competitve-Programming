class Solution:
    def addDigits(self, num: int) -> int:
        def solve(x:int) -> int:
            total = 0
            while x>0:
                total += (x%10)
                x = x//10
            return total

        while num > 9:
            num = solve(num)
        return num
