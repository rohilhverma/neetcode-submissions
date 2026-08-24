class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        for x in range(len(nums)):
            if nums[abs(nums[x])-1] < 0:
                return abs(nums[abs(x)])
            else:
                nums[abs(nums[x])-1]*=-1
    
        
