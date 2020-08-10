class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            ans *= 26
            ans += ord(s[i]) - ord('A') + 1
        return ans
