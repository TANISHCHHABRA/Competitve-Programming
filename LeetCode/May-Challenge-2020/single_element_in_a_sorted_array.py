class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums) == 1):
            return nums[0]
        for i in range(0, len(nums) - 1,2):
            if(nums[i] != nums[i+1]):
                return nums[i]
        if(len(nums)%2 != 0):
            return nums[len(nums)-1]
        
