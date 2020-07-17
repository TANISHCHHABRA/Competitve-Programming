class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        d = sorted(d.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
        ans = []
        for i in d:
            if k > 0:
                ans.append(i[0])
            else:
                break
            k -= 1
        return ans
