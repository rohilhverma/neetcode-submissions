class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for x in range(len(nums)):
            if target - nums[x] in d:
                return [d[target - nums[x]], x]
            d[nums[x]]=x
        