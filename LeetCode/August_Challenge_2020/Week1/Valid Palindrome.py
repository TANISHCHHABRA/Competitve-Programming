class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        ans = ""
        for i in s:
            if (i>='a' and i<='z') or (i >= '0' and i<='9'):
                ans+=i
        if (len(ans)==0) or (len(ans)==1):
            return True
        for i in range(len(ans)//2):
            if ans[i] != ans[-i-1]:
                return False
        return True
