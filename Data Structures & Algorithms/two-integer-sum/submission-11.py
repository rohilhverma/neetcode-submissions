class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for x in range(len(nums)):
            if target - nums[x] in dct:
                return [dct[target-nums[x]],x]
            dct[nums[x]] = x
