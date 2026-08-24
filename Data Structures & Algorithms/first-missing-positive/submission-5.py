class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        
        for x in range(len(nums)):
            if nums[x]<=0 or nums[x] > len(nums):
                nums[x]=len(nums)+1
            #no 0's or negatives
        for x in range(len(nums)):
            if abs(nums[x])<=len(nums):
                if nums[abs(nums[x]) -1]<0:
                    continue
                else:
                    nums[abs(nums[x]) -1]*=-1
        for x in range(len(nums)):
            if nums[x]>0:
                return x+1
        return len(nums)+1
            