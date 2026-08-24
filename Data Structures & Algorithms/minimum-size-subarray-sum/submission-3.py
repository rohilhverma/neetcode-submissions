class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        s=0
        m=0
        for x in range(len(nums)):
            s += nums[x]
            if s >= target:
                while l < len(nums) and s >= target:
                    s-=nums[l]
                    l+=1
                if m>0:
                    m=min(m,x-l+2)
                else:
                    m=x-l+2
        return m