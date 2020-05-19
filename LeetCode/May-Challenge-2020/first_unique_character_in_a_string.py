class Solution:
    def firstUniqChar(self, s: str) -> int:
        od = OrderedDict()
        for i in s:
            if i in od:
                od[i] += 1
            else:
                od[i] = 1
        a = ''
        for i in od:
            if od[i] == 1:
                a = i
                break
        c = 0
        for i in s:
            if i == a:
                return c
            c += 1
        return -1
