class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for x in range(len(nums)):
            if nums[x] < 0:
                nums[x]=0
            
        for x in range(len(nums)):  
            if 0 < abs(nums[x]) < len(nums)+1:
                bound=abs(nums[x])-1
                if nums[bound]>0:
                    nums[bound]*=-1
                elif nums[bound]==0:
                    nums[bound]=-1*(len(nums)+1)
        
        for x in range(len(nums)):
            if nums[x] >= 0:
                return x+1
        return len(nums)+1