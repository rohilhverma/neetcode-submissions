class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        lst=[0,]*len(nums)

        for x in nums:
            if lst[x-1] > 0:
                return x
            else:
                lst[x-1] = 1
        
