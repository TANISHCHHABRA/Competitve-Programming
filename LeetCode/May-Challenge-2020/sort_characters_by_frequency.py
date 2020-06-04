class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        s = list(s)

        result = [item for items, c in Counter(s).most_common() for item in [items] * c]

        s = ""
        for i in result:
            s = s + i
        return s
