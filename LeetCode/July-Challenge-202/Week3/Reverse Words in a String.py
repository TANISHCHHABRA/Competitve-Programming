class Solution:
    def reverseWords(self, s: str) -> str:
        s =  s.split()[::-1]
        if len(s) == 0:
            return ""
        l = ""
        for i in range(len(s)-1):
            l += s[i]
            l+=' '
        l += s[len(s)-1]
        return l
