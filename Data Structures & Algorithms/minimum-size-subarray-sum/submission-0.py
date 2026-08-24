class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length=100001
        l=0
        sum=0
        for x in range(len(nums)):
            sum+=nums[x]
            while sum >= target:
                length=min(x-l+1,length)
                sum -= nums[l]
                l+=1
            
        if (length == 100001):
            return 0
        if (length):
            return length
        
        
