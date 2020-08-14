class Solution:
    def longestPalindrome(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        count = 0
        c = False
        while True:
            flag = True
            for i in d:
                if d[i] >= 2:
                    d[i] -= 2
                    count += 2
                    flag = False
                elif d[i] == 1:
                    c = True
            if flag:
                break
        if c:
            count += 1
        return count
