class Solution:
    def toGoatLatin(self, S: str) -> str:
        l = ['a','i','e','o','u','A','I','E','O','U']
        s = S.split()
        for i in range(len(s)):
            if s[i][0] in l:
                s[i] += 'ma'
            else:
                s[i] += s[i][0]
                s[i] = s[i][1:]
                s[i] += 'ma'
            s[i] += 'a'*(i+1)
        S = ""
        for i in range(len(s)-1):
            S += s[i]
            S += " "
        S += s[-1] 
        return S
