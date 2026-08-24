class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        rollingSum=0
        y=0
        m=float("inf")
        for x in range(len(nums)):
            rollingSum += nums[x]
            if rollingSum >= target:
                while rollingSum>=target:
                    m=min(x-y+1,m)
                    rollingSum-=nums[y]
                    y+=1

        return 0 if sum(nums) < target else m