class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        citations.sort()
        n = len(citations)
        max_ = 0
        if n <= citations[0]:
            return n
        for i in range(1, n+1):
            idx = bisect.bisect_left(citations, i)
            n_rest = n - idx 
            if n_rest >= i:
                max_ = max(max_, i)
        return max_
