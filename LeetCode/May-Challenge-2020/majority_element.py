class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        od = OrderedDict()
        for i in nums:
            if i in od:
                od[i] += 1
            else:
                od[i] = 1
        n = len(nums)
        for i in od:
            if od[i] > n/2:
                return i
