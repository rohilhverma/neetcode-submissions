class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        val = 0
        for x in nums:
            if count == 0 or x == val:
                val = x
                count += 1
            else:
                count -= 1
        return val
            