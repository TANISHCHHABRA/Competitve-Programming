class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        ans = []
        odd = []
        for i in A:
            if i%2 == 0:
                ans.append(i)
            else:
                odd.append(i)
        for i in odd:
            ans.append(i)
        return ans
