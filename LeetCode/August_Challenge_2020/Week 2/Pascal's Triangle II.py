class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        k = rowIndex
        if k == 0:
            return [1]
        if k == 1:
            return [1,1]
        l = [1,1]
        for _ in range(k-1):
            r = [1] + [l[j] + l[j+1] for j in range(len(l) - 1)] + [1]
            l = r
        return l
